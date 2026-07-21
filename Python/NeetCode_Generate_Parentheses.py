def generateParanthesis(n: int) -> List[str]:
    def aux(curr_string: str, opened: int, unused: int):
        if opened == 0 and unused == 0:
            return [curr_string]

        open_new = []
        if unused > 0:
            open_new = aux(curr_string + "(", opened + 1, unused - 1)

        close_old = []
        if opened >= 1:
            close_old = aux(curr_string + ")", opened - 1, unused)

        return open_new + close_old

    return aux("", 0, n)
