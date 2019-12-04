from voc_eval import voc_eval

print voc_eval('C:\yolo-gpu\darknet-master\build\darknet\x64\results\{}.txt', 'C:\yolo-gpu\darknet-master\build\darknet\x64\YOLOV3_0928\data\xml\{}.xml', 'C:\yolo-gpu\darknet-master\build\darknet\x64\YOLOV3_0928\data\main\test.txt', 'person', '.')