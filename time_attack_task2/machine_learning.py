import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

imgs = cv2.imread('Untitled.jpeg')
print('원본 이미지 크기: ', imgs.shape)

results = model(imgs)

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6] == 'person']

# print(result)

tmp_img_all = cv2.imread('Untitled.jpeg')
tmp_img = cv2.imread('Untitled.jpeg')

for i in range(5):
    cropped = tmp_img[int(result[i][1]):int(result[i][3]),
                      int(result[i][0]):int(result[i][2])]
    # print("crop", cropped.shape)
    cv2.imwrite(f'people{i}.png', cropped)

    cv2.rectangle(tmp_img_all, (int(results.xyxy[0][i][0].item()), int(results.xyxy[0][i][1].item())), (int(
        results.xyxy[0][i][2].item()), int(results.xyxy[0][i][3].item())), (255, 255, 255))
    cv2.imwrite('result1.png', tmp_img_all)
# print(results.pandas().xyxy[0])
