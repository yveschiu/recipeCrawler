from functools import wraps, partial
import time

def countTimeDecorator(init_func=None, *, time_unit="sec"):

    if init_func == None:
        return partial(countTimeDecorator, time_unit=time_unit)

    @wraps(init_func)
    def countTime(*pos_args, **kw_args):
        """This decorator can count the time spent for the function decorated"""
        time_start = time.time()
        return_value = init_func(*pos_args, **kw_args)
        time_end = time.time()

        if time_unit == "sec" or "s":
            time_used = (time_end-time_start)
        if time_unit == "min" or "m":
            time_used = (time_end-time_start) / 60
        if time_unit == "hour" or "h":
            time_used = (time_end - time_start) / 60 / 60

        print("{}'s time consumed({}) is: {}".format(init_func.__name__, time_unit, str(time_used)))

        return return_value

    return countTime


if __name__ == "__main__":
    countTimeDecorator()

# --------------------------------------------------------------

# from functools import wraps, partial
# import time

# def time_count_decorator(init_func=None, *, time_unit='sec'):
#     if init_func is None:
#         return partial(time_count_decorator, time_unit=time_unit)
#
#     @wraps(init_func)
#     def time_count(*pos_args, **kw_args):
#         ''' The docstring of time_count '''
#         ts = time.time()
#         return_value = init_func(*pos_args, **kw_args)
#         te = time.time()
#
#         if time_unit == 'sec':
#             time_used = te - ts
#
#         elif time_unit == 'min':
#             time_used = (te - ts) / 60
#
#         elif time_unit == 'hour':
#             time_used = (te - ts) / 60 / 60
#
#         print("{}'s time consume({}): {}".format(init_func.__name__, time_unit, time_used))
#
#         return return_value
#
#     return time_count