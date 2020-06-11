def count_matches(package_names):
    matches = [p for p in package_names if 'pink'.casefold() in p.casefold() or 'rose'.casefold() in p.casefold()]
    return len(matches)

test_input = """
pink
tequilaSunrose
mExicanPInK
Coquelicot
turqrose
roSee
JETblack
pink
babypink
pInKpinkPinK
PInkrose
lazerlemon
""".split()

nomatches = """
Coquelicot
JETblack
""".split()


assert count_matches(test_input) == 9

assert count_matches(nomatches) == 0


package_names = []
num_packages = int(input())

for _ in range(num_packages):
    package_names.append(input())

num_matches = count_matches(package_names)

if num_matches:
    print(num_matches)
else:
    print('I must watch Star wars with my daughter')