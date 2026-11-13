import math

def split_degrees(eq):
    if eq == "0":
        return {}
    parts = []
    buf = ""
    for i in range(len(eq)):
        if eq[i] == "+":
            parts.append(buf.strip())
            buf = ""
        elif eq[i] == "-":
            parts.append(buf.strip())
            buf = "-"
        elif eq[i] != " ":
            buf += eq[i]
    parts.append(buf.strip())
    parts = [part for part in parts if part]
    degrees = {}
    for part in parts:
        nb, deg = map(str.strip, part.split("*"))
        if deg[2:] in degrees:
            degrees[int(deg[2:])] += float(nb)
        else:
            degrees[int(deg[2:])] = float(nb)
    return degrees


class Computor:
    def __init__(self, eq):
        print(eq)
        self.eq = eq
        splitted = self.eq.split("=")
        left = split_degrees(splitted[0].strip())
        right = split_degrees(splitted[1].strip())
        for deg, val in right.items():
            if deg in left:
                left[deg] -= val

        self.show_reduce(left)
        degree = self.get_degree(left)



        if degree == 0:
            if left[0] == 0:
                print("Any real number is a solution.")
            else:
                print("No solution.")
            return

        print("Polynomial degree:", degree)

        if degree == 1:
            print("The solution is:")
            x1 = -left[0] / left[1]
            print(x1)

        if degree == 2:
            a = left[2]
            b = left[1]
            c = left[0]
            delta = b**2 - 4*a*c
            if delta == 0:
                print("Discriminant is strictly positive, the two solutions are:")
                solution = -b/(2 * a)
                print(solution)

            if delta > 0:
                print(a, b, c, delta)
                print("Discriminant is strictly positive, the two solutions are:")
                x1 = (-b - math.sqrt(delta))/(2 * a)
                print(x1)
                x2 = (-b + math.sqrt(delta))/(2 * a)
                print(x2)
            if delta < 0:
                print("i")
        if degree > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve.")

    def show_reduce(self, exp):
        print("Reduced form: ", end="")
        for i, (deg, val) in enumerate(exp.items()):
            sign = "+ " if val > 0 and i > 0 else ""
            print(f"{sign}{val} * X^{deg} ", end="")
        print("= 0")

    def get_degree(self, degrees):
        return max(degrees)







def main():
    Computor("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
    print("\n")
    Computor("5 * X^0 + 4 * X^1 = 4 * X^0")
    print("\n")
    Computor("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
    print("\n")
    Computor("6 * X^0 = 6 * X^0")
    print("\n")
    Computor("10 * X^0 = 15 * X^0")
    print("\n")
    Computor("1 * X^0 + 2 * X^1 + 5 * X^2 = 0")


if __name__ == "__main__":
    main()

