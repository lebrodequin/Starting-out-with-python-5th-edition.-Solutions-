room_dict = {
    'CS101' : 3004,
    'CS102' : 4501,
    'CS103' : 6755,
    'NT110' : 1244,
    'CM241' : 1411
    }

instructor_dict = {
    'CS101': 'Haynes',
    'CS102': 'Alvardo',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

meeting_time_dict = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '12:00 p.m.'
}

print(room_dict.keys())
course_number = input('input course number: ')
print(f'course room number\t{room_dict.get(course_number)}\n'
      f'instructor\t\t\t{instructor_dict.get(course_number)}\n'
      f'meeting time\t\t{meeting_time_dict.get(course_number)}')