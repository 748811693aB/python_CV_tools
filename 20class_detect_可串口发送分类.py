import sensor,image,lcd,time
import KPU as kpu

lcd.init(type=2)
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_vflip(1) #flip camera; maix go use sensor.set_hmirror(0)
sensor.set_hmirror(1)
sensor.set_vflip(1)
sensor.run(1)
clock = time.clock()
classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
task = kpu.load(0x800000)
anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

###########UART#################
from fpioa_manager import fm
fm.register(5, fm.fpioa.UART1_TX, force=True)
fm.register(4, fm.fpioa.UART1_RX, force=True)
from machine import UART
uart_A = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=4096) #parity,stop
import time
from fpioa_manager import fm
from Maix import GPIO
io_led_red = 14
fm.register(io_led_red, fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
time.sleep_ms(100) # wait uart ready
####################################

while(True):
    clock.tick()
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    print(clock.fps())
    if code:
        for i in code:
            a=img.draw_rectangle(i.rect())
            a = lcd.display(img)
            for i in code:
                lcd.draw_string(i.x(), i.y(), classes[i.classid()], lcd.RED, lcd.WHITE)
                lcd.draw_string(i.x(), i.y()+12, '%f1.3'%i.value(), lcd.RED, lcd.WHITE)
                uart_A.write(classes[i.classid()])#(b'\r\n0101\r\n')
                uart_A.write('\r\n')
                led_r.value(1)
    else:
        a = lcd.display(img)
        led_r.value(0)
a = kpu.deinit(task)

uart_A.deinit()
del uart_A

