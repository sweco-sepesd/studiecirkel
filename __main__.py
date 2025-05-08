import importlib
import pkgutil
package = pkgutil.resolve_name(__package__)
for module_info in pkgutil.walk_packages(package.__path__):
    if module_info.name == __name__:
        #silly me...
        continue
    qname = '.'.join([package.__name__, module_info.name])
    module = importlib.import_module(qname)
    try:
        function = getattr(module, 'hello')
        print('-'*80)
        print('Module:', module_info.name)
        print(module.__doc__)
        print(function.__name__)
        print(function.__doc__)
        print('-'*80)
        val = function()
        print(val)
    except AttributeError as e:
        print(e)