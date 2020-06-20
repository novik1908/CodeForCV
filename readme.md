Добрый день!
Объясняю, для чего нужны программы и как они работают:
1. GenerateCoordsForFigureWithMovingIt.py

    1.1 генерирует фигуру, которая представляет собой множество точек, это множество будет разным каждый раз после каждого запуска программы

    1.2 двигает эту фигуру на указанное растояние
    
     пример:
     
    ![Пример работы программы 1](https://github.com/novik1908/CodeForCV/raw/master/image/primer1.png)
2. RoomSnapshot and RotateRoom.py
   
    2.1 читает файл csv, в котором находятся считаные лидаром реальные координаты комнаты
   
    2.2 поворчивает эту комнату на указанный угол (угол может быть отрицательным)
 
     пример:
     
    ![Пример работы программы 2](https://github.com/novik1908/CodeForCV/raw/master/image/primer2_1.png)
    ![Пример работы программы 2](https://github.com/novik1908/CodeForCV/raw/master/image/primer2_2.png)
3. VisualizeAllCoordsInDirectoryFronmTXT.py

    3.1 читает все файлы txt с координатами в указанной директории(папке)
   
    3.2 переводит координаты из радиальной системы исчисления в нормальную
   
    3.3 на выбор выводит данные на консоль либо рисует получившуюся фигуру в mathplotlib

     пример:
     
    ![Пример работы программы 3](https://github.com/novik1908/CodeForCV/raw/master/image/primer3.png)
4. VisualizeVisorCoordsFromCSV.py

    4.1 снимает значения из указанного файла csv (то, что снял лидар в реальной жизни), конвертирует координаты из из радиальной системы исчисления в нормальную и выводит результат на выбор: консоль либо визуально в mathplotlib

     пример:
     
    ![Пример работы программы 4](https://github.com/novik1908/CodeForCV/raw/master/image/primer4_1.png)
    ![Пример работы программы 4](https://github.com/novik1908/CodeForCV/raw/master/image/primer4_2.png)
    
Прим.: 
1. В каждом файле csv - 5тыс. точек, первые версии программы очень долго обрабатывали такое количество, теперь обработка занимает примерно 0,5сек (считал с помощью библиотеки time)

2. Лидар - прибор, который показывает границы объектов, например границы комнаты, в которой он находится, в радиальной системе координат (угол, длина) и выводит результат в файл любого формата (я использовал txt и csv)
