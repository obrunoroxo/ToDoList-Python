class CreateBoardNameError(Exception):
    def __str__(self) -> str:
        return 'Nome passado já existente ou semelhante, tente outro nome!'


class CreateListNameError(Exception):
    def __str__(self) -> str:
        return 'Nome passado já existente ou semelhante, tente outro nome!'


class CreateTaskNameError(Exception):
    def __str__(self) -> str:
        return 'Nome passado já existente ou semelhante, tente outro nome!'