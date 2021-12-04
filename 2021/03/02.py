import reprlib
from typing import List, Tuple


def frame_diag_report():
    diag_report = []
    with open("input.txt") as inp:
        while True:
            try:
                diag_report.append(list(map(int, inp.readline().split()[0])))
            except IndexError:
                break
    return diag_report


def bisect_array(array: List[List[int]], bit: int):
    return list(filter(lambda lst: not lst[bit], array)), list(filter(lambda lst: lst[bit], array))


def life_support_rating(diag_report: List[List[int]]) -> int:
    zero_bit_list, one_bit_list = bisect_array(diag_report, 0)
    if len(zero_bit_list) > len(one_bit_list):
        oxy_rating = o2_gen_rating(zero_bit_list, 1)
        co2_rating = co2_scrub_rating(one_bit_list, 1)
    else:
        oxy_rating = o2_gen_rating(one_bit_list, 1)
        co2_rating = co2_scrub_rating(zero_bit_list, 1)

    return oxy_rating * co2_rating


def co2_scrub_rating(co2_scrub_data: List[List[int]], bit):
    if len(co2_scrub_data) == 1:
        return num_frm_binlist(*co2_scrub_data)

    zero_bit_list, one_bit_list = bisect_array(co2_scrub_data, bit)
    if len(zero_bit_list) > len(one_bit_list):
        return co2_scrub_rating(one_bit_list, bit + 1)
    else:
        return co2_scrub_rating(zero_bit_list, bit + 1)


def o2_gen_rating(oxygen_gen_data: List[List[int]], bit):
    if len(oxygen_gen_data) == 1:
        return num_frm_binlist(*oxygen_gen_data)

    zero_bit_list, one_bit_list = bisect_array(oxygen_gen_data, bit)
    if len(zero_bit_list) > len(one_bit_list):
        return o2_gen_rating(zero_bit_list, bit + 1)
    else:
        return o2_gen_rating(one_bit_list, bit + 1)


def num_frm_binlist(binlist: List[int]) -> int:
    return int(''.join(map(str, binlist)), 2)


def bin_diag():
    diag_report = frame_diag_report()
    rating = life_support_rating(diag_report)
    print(f"Life Support Rating: {rating}")


if __name__ == '__main__':
    bin_diag()
