'''****************************************************
 File:     lists_optimization.py
 Author:   (c) Paulo Martins
 Date:     20130828
 Desc:     best method to return first value from a list of tuples
 version:  1.0
 Change Log:
****************************************************'''
import random
import string
from timeit import Timer
import profile, cProfile, pstats, io


def test_a(any_list, value_to_look):
    res = None
    res = filter(lambda x: value_to_look in x, any_list)
    if res is not None:
        res = res[0][1]
    return res


def test_b(any_list, value_to_look):
    res = None
    res = [s for s in any_list if value_to_look in s]
    if res is not None:
        res = res[0][1]
    return res


def test_c(any_list, value_to_look):
    # create dict from list like ['a':0, 'b':1]
    any_dict = dict(any_list)
    if value_to_look in any_dict:
        return any_dict[value_to_look]
    else:
        return None


def run_test(any_list, value_to_look):
    t = Timer("test_a(" + str(any_list) + "," + str(value_to_look) + ")", "from __main__ import test_a")
    print t.timeit()
    t = Timer("test_b(" + str(any_list) + "," + str(value_to_look) + ")", "from __main__ import test_b")
    print t.timeit()
    t = Timer("test_c(" + str(any_list) + "," + str(value_to_look) + ")", "from __main__ import test_c")
    print t.timeit()


def run_test_with_profile(any_list, value_to_look):
    #pr = cProfile.Profile()
    #pr.enable()
    #test_a(any_list_x, value_to_look_z)
    #pr.disable()
    #s = io.StringIO()
    #ps = pstats.Stats(pr, stream=s)
    #print ps
    #print cProfile.run("test_b(" + str(any_list) + "," + str(value_to_look) + ")")
    print profile.run("test_a(" + str(any_list) + "," + str(value_to_look) + ")")
    print profile.run("test_b(" + str(any_list) + "," + str(value_to_look) + ")")
    print profile.run("test_c(" + str(any_list) + "," + str(value_to_look) + ")")


def main():
    # create list like [(0, 'a'), (1, 'b')]
    #x = [i for i in range(10)]
    #x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = string.ascii_lowercase
    a = string.printable
    b = [i for i in range(len(a))]
    any_list_x = zip(b, a)
    print any_list_x
    tuple_to_look_z = random.choice(any_list_x)
    value_to_look_z = tuple_to_look_z[0]
    print 'value_to_look: %s' % value_to_look_z
    print test_a(any_list_x, value_to_look_z)
    print test_b(any_list_x, value_to_look_z)
    print test_c(any_list_x, value_to_look_z)
    run_test(any_list_x, value_to_look_z)
    #run_test_with_profile(any_list_x, value_to_look_z)


if __name__ == "__main__":
    #print profile.run('main()')
    main()
