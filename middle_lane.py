from re import X
from turtle import width
import cv2
from cv2 import circle
import numpy as np
import matplotlib.pyplot as plt

min_line_len = 20  # 线的最小长度
max_line_gap = 40  # 线段之间最大允许间隙
slope_threshold_min = 0.2  # 斜率检测参数
slope_threshold_max = 10
distance_threshold = 5  # 间距参数
exc_time = [-1.0, -1.0]

rho = 1  # 霍夫变换参数
theta = np.pi / 180
threshold = 15


####################################################################################################################
# 划分左右车道
def choose_lines(lines, slope_threshold_min, slope_threshold_max):
    left_lines, right_lines = [], []
    k=0
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 != x2:
                k = float(y1 - y2) / (x1 - x2)
                if abs(k) < slope_threshold_max and abs(k) > slope_threshold_min:
                    if k < 0:
                        if ((x1 + x2)/2) > 200:
                            continue
                        left_lines.append(line)
                    elif k > 0:
                        right_lines.append(line)
                else:
                    continue

    return left_lines, right_lines, k


def get_lane_info(input_roi_edges, input_cv_img):
    h = input_roi_edges.shape[0]
    lines = hough_lines(input_roi_edges, rho, theta, threshold, min_line_len, max_line_gap)
    drawing = np.zeros((input_cv_img.shape[0], input_cv_img.shape[1], 3), dtype=np.uint8)

    left_results, right_results, middle_results = [], [], []
    k=0
    if lines is not None:
        left_lines, right_lines, k = choose_lines(lines, slope_threshold_min, slope_threshold_max)
        if len(left_lines) > 0:
            #select_points(h, left_lines, distance_threshold)

            left_points = [(x1, y1) for line in left_lines for x1, y1, x2, y2 in line]
            left_points = left_points + [(x2, y2) for line in left_lines for x1, y1, x2, y2 in line]
            left_results = least_squares_fit(left_points, 0, input_cv_img.shape[0])

            #cv2.line(drawing, left_results[0], left_results[1], (0, 0, 255), 4)  # 红色

        if len(right_lines) > 0:
            #select_points(h, right_lines, distance_threshold)

            right_points = [(x1, y1) for line in right_lines for x1, y1, x2, y2 in line]
            right_points = right_points + [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]
            right_results = least_squares_fit(right_points, 0, input_cv_img.shape[0])

            #cv2.line(drawing, right_results[0], right_results[1], (0, 255, 0), 4)  # 绿色

        result = None
        #result = cv2.addWeighted(input_cv_img, 0.5, drawing, 0.5, 0)
    else:
        result = input_cv_img
        
    #cv2.putText(result, str("k: %.3f"%k), (20, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0),2)
    
    return result, left_results, right_results

def get_turn_error(input_cv_img, left_results, right_results):
    global conner_flag
    global cnt_sensor
    global start_cnt
    global start_x
    
    height = input_cv_img.shape[0]  # HWC rows cols C
    width = input_cv_img.shape[1]  # HWC rows cols C

     
    if len(left_results) > 0 and len(right_results) > 0:
        X = (left_results[1][0] + right_results[1][0]) / 2
                             
        Turn_error = (width / 2 - X)*0.90
    # 只有右线-----左转
    elif len(left_results) == 0 and len(right_results) != 0:
        X_top = right_results[0][0]
        X_bottom = (height - right_results[0][1]) * (right_results[0][0] - right_results[1][0])/(right_results[0][1] - right_results[1][1]) + right_results[0][0]
        X = (X_top - 80) / 2 + (X_bottom -220) / 2
        Turn_error = (width / 2 - X)  # Turn left

    # 只有左线-----右转
    elif len(right_results) == 0 and len(left_results) != 0:
        X_top = left_results[0][0]
        X_bottom = (height - left_results[0][1]) * (left_results[0][0] - left_results[1][0])/(left_results[0][1] - left_results[1][1]) + left_results[0][0]
        X = (X_top + 80) / 2 + (X_bottom + 220) / 2
        Turn_error = (width / 2 - X)*0.84  # negative(Turn right)
        
    else:
        X = 0
        Turn_error = 0

    return Turn_error

# 在图像中选出最密集的直线，删除零散的直线
def select_points(rows, line_list, distance_threshold):
    max_count = 0
    xmin_points = [(x2 - x1) / (y2 - y1) * (rows - y1) + x1 for line in line_list for x1, y1, x2, y2 in line]
    standard_num = xmin_points[0]
    for i in range(0, len(xmin_points), 1):
        count = 0
        for points in xmin_points:
            if xmin_points[i] - distance_threshold < points < xmin_points[i] + distance_threshold:
                count = count + 1
        if count > max_count:
            standard_num = xmin_points[i]
            max_count = count
    list_del_index = []
    for i in range(0, len(xmin_points), 1):
        if xmin_points[i] < standard_num - distance_threshold or xmin_points[i] > standard_num + distance_threshold:
            list_del_index.append(i)
    counter = 0
    if len(list_del_index) > 0:
        for index in list_del_index:
            index = index - counter
            line_list.pop(index)
            counter += 1

# 最小二乘法拟合
def least_squares_fit(point_list, ymin, ymax):
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]

    # polyfit第三个参数为拟合多项式的阶数，所以1代表线性
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)  # 获取拟合的结果

    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))

    return [(xmin, ymin), (xmax, ymax)]

# 统计概率霍夫直线变换
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold,
                            minLineLength=min_line_len, maxLineGap=max_line_gap)
    return lines

################################################################################################################




H_min = 22  # HSV提取
H_max = 100#74
S_min = 100
S_max = 255
V_min = 0
V_max = 255

colorLow = np.array([H_min, S_min, V_min])
colorHigh = np.array([H_max, S_max, V_max])
hsv_image = cv2.imread("turn.jpg", flags=1)  # flags=1 读取彩色图像(BGR)
hsv_image_orin = cv2.imread("turn.jpg", flags=1)
hsv_image_orin = cv2.cvtColor(hsv_image_orin,cv2.COLOR_BGR2RGB)
frame_binary = cv2.inRange(hsv_image, colorLow, colorHigh)  # 图像二值化

# 11.12 霍夫变换直线检测
#img = cv2.imread("turn-HSV_inRange.jpg", flags=1)  # flags=1 读取为彩色图像
img = frame_binary
height = img.shape[0]
weidth = img.shape[1]
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray = frame_binary
hImg, wImg = imgGray.shape

# Canny 边缘检测， kSize 为高斯核大小，t1, t2为阈值大小
ratio, low = 3, 120
imgGauss = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgCanny = cv2.Canny(imgGauss, low, low*ratio)
pEdge = np.where(imgCanny==255)  # 所有的边缘像素
print(hImg, wImg, imgCanny.max(), imgCanny.min(), len(pEdge[0]))


left_results, right_results, middle_results = [], [], []
roi_edges = img
cv_image = img


result, left_results, right_results = get_lane_info(imgCanny, cv_image)

print("left_results = ",left_results)
print("right_results = ",right_results)
cv2.line(hsv_image, left_results[0],left_results[1], (0, 0, 255),10)  # 绘制直线
cv2.line(hsv_image, right_results[0],right_results[1], (0, 0, 255),10)

Turn_error = get_turn_error(cv_image, left_results, right_results)
X = (left_results[0][0] + right_results[0][0]) / 2

#cv2.circle(hsv_image,(int(X),int(height/2)),10,(0, 0, 255),-1,)

print("img_shape = ",height,weidth)
print("center_point = ",int(X),int(weidth/2))
print("Turn error = ",Turn_error)

plt.figure(figsize=(9, 5))
plt.subplot(131), plt.title("Origin"), plt.imshow(hsv_image_orin, cmap='gray'), plt.axis('off')
plt.subplot(132), plt.title("Hough"), plt.imshow(cv2.cvtColor(hsv_image, cv2.COLOR_RGB2BGR)), plt.axis('off')
plt.tight_layout()
plt.show()




