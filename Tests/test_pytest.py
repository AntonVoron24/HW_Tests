import pytest
from main import max_stat, unique_values, russian_visit

FIXTURE_max_stat = [
	({'facebook': 55, 'yandex': 120, 'vk': 115}, 'yandex'),
	({'google': 99, 'email': 42, 'ok': 98, 'instagram': 158}, 'instagram')
]


@pytest.mark.parametrize("stats, etalon", FIXTURE_max_stat)
def test_max_stat(stats, etalon):
	result = max_stat(stats)
	assert result == etalon


FIXTURE_unique_values = [
	(
		{
			'user1': [213, 15, 213],
			'user2': [54, 119, 119],
			'user3': [213, 98, 98, 35]
		},
		[98, 35, 15, 213, 54, 119]
	),
	(
		{
			'user1': [555, 555, 112],
			'user2': [999, 676, 666],
			'user3': [111, None, 111]
		},
		[676, 999, 555, 111, 112, 666, None]
	)
]


@pytest.mark.parametrize("id_dict, etalon", FIXTURE_unique_values)
def test_unique_values(id_dict, etalon):
	result = unique_values(id_dict)
	assert result == etalon


FIXTURE_russian_visit = [
	(
		[
			{'visit1': ['Москва', 'Россия']},
			{'visit2': ['Дели', 'Индия']}
		], [{'visit1': ['Москва', 'Россия']}]
	),
	(
		[
			{'visit4': ['Лиссабон', 'Португалия']},
			{'visit5': ['Париж', 'Франция']}
		], [])
]


@pytest.mark.parametrize("visit_list, etalon", FIXTURE_russian_visit)
def test_russian_visit(visit_list, etalon):
	result = russian_visit(visit_list)
	assert result == etalon
