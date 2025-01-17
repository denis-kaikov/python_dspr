# HW-02. Исслледование данных HR агенства

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)  
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Цели исследования](README.md#Цели-исследования)  
[4. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[5. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[6. Результат](README.md#Результаты)    


### Описание проекта    
[Исслледование данных HR агенства](https://github.com/denis-kaikov/python_dspr/blob/main/HW-02/HR_trends.ipynb) 



### Какой кейс решаем?    
HR-агентство изучает тренды на рынке труда в IT. Компания хочет провести исследование на основе данных о зарплатах в сфере Data Science за 2020–2022 годы и получить некоторые выводы.

### Цели исследования
В ходе анализа предстоит ответить на следующие вопросы:

- Наблюдается ли ежегодный рост зарплат у специалистов Data Scientist?
- Как соотносятся зарплаты Data Scientist и Data Engineer в 2022 году?
- Как соотносятся зарплаты специалистов Data Scientist в компаниях различных размеров?
- Есть ли связь между наличием должностей Data Scientist и Data Engineer и размером компании?

### Краткая информация о данных
- work_year	Год, в котором была выплачена зарплата.
- experience_level	Опыт работы на этой должности в течение года со следующими возможными значениями:
    - EN — Entry-level/Junior;
    - MI — Mid-level/Intermediate;
    - SE — Senior-level/Expert;
    - EX — Executive-level/Director.
- employment_type	Тип трудоустройства для этой роли:
    - PT — неполный рабочий день;
    - FT — полный рабочий день;
    - CT — контракт;
    - FL — фриланс.
- job_title	Роль, в которой соискатель работал в течение года.
- salary	Общая выплаченная валовая сумма заработной платы.
- salary_currency	Валюта выплачиваемой заработной платы в виде кода валюты ISO 4217.
- salary_in_usd	Зарплата в долларах США (валютный курс, делённый на среднее значение курса доллара США за соответствующий год через fxdata.foorilla.com).
- employee_residence	Основная страна проживания сотрудника в течение рабочего года в виде кода страны ISO 3166.
- remote_ratio	Общий объём работы, выполняемой удалённо. Возможные значения:
    - 0 — удалённой работы нет (менее 20 %);
    - 50 — частично удалённая работа;
    - 100 — полностью удалённая работа (более 80 %).
- company_location	Страна главного офиса работодателя или филиала по контракту в виде кода страны ISO 3166.
- company_size	Среднее количество людей, работавших в компании в течение года:
    - S — менее 50 сотрудников (небольшая компания);
    - M — от 50 до 250 сотрудников (средняя компания);
    - L — более 250 сотрудников (крупная компания).

### Этапы работы над проектом  
- проведена предобработка данных для их удобного использования 
- проведен первичный рзведывательный анализ данных для поиска возможных взаимосвязей и нахождени возможных выбросов
- произведена очистка данных от выобросов дубликатов и пропусков
- выдвинуты гипотезы о возможных зависимостях между признаками и их влияние на итоговый уровень заработной платы 
- проведены тесты для подтверждения выдвинутых гипотезы 
- оформлены окончательные потвержденные гипотезы

### Результаты:  
Сделаны следующие выводы по работе:
- у нас недостаточно данных, чтобы говорить о ежегодном повышении ЗП для специалистов data science
- у специалистов DS и DE в 2022 зарплаты не отличаются 
- зп зависит от величины компании, причем в средних платят больше всего, в малых - меньше всего 
- Есть связь между наличием должности и размером компании
- ЗП специалистов DS прямо пропорциональна опыту работы
- специалистам на частичной удаленке зачастую платят меньше чем остальным
- с увеличением размера компании, растет процент работников на частичной удаленке (конкретно мидов и менеджеров(директоров)) 
- соотношение зп за удаленку и работу в офисе напрямую зависит от величины компании, причем:
    - В крупных за работу в офисе платят больше (меньше джунов относительно низкими зп)
    - В средних за удаленку платят больше 
    - В малых разницы нет 
- Для всех размеров компаний удаленка предпочтительнее 



