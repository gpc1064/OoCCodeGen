from devito import Grid, TimeFunction, Function, Eq, Operator

grid = Grid(shape=(200, 200, 200))

u = TimeFunction(name="u", grid=grid, space_order=2)

eq = Eq(u.forward, u.dx)

op = Operator(eq, opt=('noop', {'out-of-core': True}), name="apply_kernel")

#op.apply(time_M=10)

print(op)
