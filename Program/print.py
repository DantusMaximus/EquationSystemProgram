class Print:
    @staticmethod
    def print_sollution(sol):
        lan = len(sol[0].lh_s)
        for val in sol:
            for i in range(0, lan):
                if val.lh_s[i] != 0:
                    print(f"x{i} = {val.rh_s}")