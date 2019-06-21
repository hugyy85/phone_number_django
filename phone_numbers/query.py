from .models import Numbers, User
import re
import bs4


# def find_last_id():
#     query = Numbers.objects.values('id_process').order_by('-id_process')[0]
#     return query['id_process'] + 1


def how_long_month(numbers=[], who_call=None, id_process=1, work_time=(8, 18)):
    result = []

    # query = Numbers.objects.all().filter(id_process=id_process, number=number)

    for number in numbers:
        time_result = 0
        internet_result = 0
        for j in number.data:
            long = j[3].split(':')
            time = j[1].split(':')

            if work_time[0] < int(time[0]) < work_time[1]:
                try:
                    time_result += (int(long[0]) * 60) + int(long[1])
                except IndexError:
                    pass
                except ValueError:
                    internet_result += int(j[3].split('Kb')[0])
        result.append('{} - Проговорил {} часа, Интернета потратил {} Mb \n').format(number.number, round(time_result / 3600, 2), round(internet_result / 1024, 2) )

    return result


def parse_phones(files=[], id_process=1):
    numbers = []
    for file in files:
        file = file.read().decode()
        num = re.findall(r'7\d{10}', file)
        soup = bs4.BeautifulSoup(file, 'lxml')
        rows = soup.tbody
        num = User(num[0], id_process)

        for row in rows:
            res = row.contents
            num.data.append([res[1].next, res[2].next, res[4].next, res[9].next])

        numbers.append(num)

    return numbers




