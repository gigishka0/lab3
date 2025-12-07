Завдання 1

    У першому потрібно реалізувати веб-сервіс для роботи з каталогом товарів.
Кожен товар описується мінімум трьома властивостями (ID, ціна, колір, вага тощо). У випадку збереження каталогу у файл параметри бажано записувати англійською.
<p></p>
Завдання 2

    У цьому завданні потрібно протестувати функціроал за допомогою Postman. Вписуємо посилання та виконуємо авторизацію через вкладку Autorezation.

<img width="1100" height="949" alt="image" src="https://github.com/user-attachments/assets/44252463-b339-4238-872a-1fec3c1f505e" />
    На рисунку бачимо  повний список товарів та їх параметри. Ім'я товару, тип та його ціна.
<p></p>
    Тепер пререглянемо один товар. У рядок вписуємо http://127.0.0.1:8000/items/1 та натискаємо send

<img width="960" height="765" alt="image" src="https://github.com/user-attachments/assets/4b015d9f-727b-4344-b1fa-1ba94280beb8" />
    На рисунку бачимо, що вивевся перший товар, а саме відеокарта.
<p></p>
    Тепер додамо товар до каталогу. Вписуємо у вкладку Body цю частину коду:
{
    "type": "RAM",
    "name": "DDR4 16GB",
    "price": 1200
}
Та перемикаємо метод GET на POST.

<img width="1143" height="1008" alt="image" src="https://github.com/user-attachments/assets/50065172-c6f4-4c0f-9328-b645a15557e1" />
<img width="509" height="138" alt="image" src="https://github.com/user-attachments/assets/efc4d5ea-e32e-4989-9598-0c4dd6e70ed6" />
<p></p>
    Тепер у списку бачимо 4 товари.
<img width="839" height="891" alt="image" src="https://github.com/user-attachments/assets/a9ae7df9-75c1-4f3a-95e8-5760a76be066" />


