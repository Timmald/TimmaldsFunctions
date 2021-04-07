from typing import Union, Optional


def findInList(searchTerm:Union[str,object],list:list[object],searchAttr:Optional[str]) -> Optional[object]:
    """Searches `list` for `searchTerm`, using `searchAttr` if necessary.

    Parameters
    --------------
    **searchTerm**(`Union[str,object]`): Either the object to search `list` for or the name of the object you are looking for in `list`
    **list**(`list[object]`): list of objects to search
    **searchAttr**(`str`): The name of the attribute representing the name of the attribute that represents the name of the object, allowing you to search the list by name instead of with a fully formed object

    Returns
    --------------
    The object with name `searchTerm`, or that is equal to `searchTerm`, in `list`, or `None` if it isn't in `list`
    """
    if isinstance(searchTerm,object):

        for item in list:
            if item==searchTerm:
                return item
    if isinstance(searchTerm,str):
        for item in list:
            if item.__getattribute__(searchAttr)==searchTerm:
                return item