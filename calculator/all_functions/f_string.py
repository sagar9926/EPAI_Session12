def f_string(fn):
    def inner(*args,**kwargs):
        result = fn(*args , **kwargs)
        args_ = [str(a) for a in args]
        kwargs_ = ['{0} = {1} '.format(k,v) for k , v in kwargs.items() ]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)
        print(f'Result of function {fn.__name__[2:]}({args_str}) = {result}')
        return result
    return inner

