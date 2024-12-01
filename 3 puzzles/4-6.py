# 4
def eFour(data):
    piles = []
    last = data

    for _ in range(data):
        piles.append(last)
        last += 2

    return piles


assert eFour(2) == [2, 4]
assert eFour(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
assert eFour(3) == [3, 5, 7]
assert eFour(17) == [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


# 5
def eFive(data):
    for i in range(int(len(data) / 2)):
        nth = i * 2

        for char in data[nth]:
            print(char)
            if char not in data[nth + 1]:
                return False
    return True


assert eFive(["a", "abb", "sfs", "sfsoo", "de", "sfde"]) is True
assert eFive(["a", "abb", "sfs", "oo", "ee", "sfde"]) is False
assert (
    eFive(["a", "abb", "sad", "ooaaesdfe", "sfsdfde", "sfsd", "sfsdf", "qwrew"])
    is False
)
assert (
    eFive(["a", "abb", "sad", "ooaaesdfe", "sfsdfde", "sfsde", "sfsdf", "qwsfsdfrew"])
    is True
)


# 6
def eSix(data):
    prev = -10
    for i in data:
        if not i == prev + 10:
            return False
        prev = i

    return True


assert (
    eSix(
        [
            0,
            10,
            20,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100,
            110,
            120,
            130,
            140,
            150,
            160,
            170,
            180,
            190,
            200,
            210,
            220,
            230,
            240,
            250,
            260,
            270,
            280,
            290,
            300,
            310,
            320,
            330,
            340,
            350,
            360,
            370,
            380,
            390,
            400,
            410,
            420,
            430,
            440,
            450,
            460,
            470,
            480,
            490,
            500,
            510,
            520,
            530,
            540,
            550,
            560,
            570,
            580,
            590,
            600,
            610,
            620,
            630,
            640,
            650,
            660,
            670,
            680,
            690,
            700,
            710,
            720,
            730,
            740,
            750,
            760,
            770,
            780,
            790,
            800,
            810,
            820,
            830,
            840,
            850,
            860,
            870,
            880,
            890,
            900,
            910,
            920,
            930,
            940,
            950,
            960,
            970,
            980,
            990,
        ]
    )
    is True
)
assert (
    eSix(
        [
            0,
            20,
            40,
            60,
            80,
            100,
            120,
            140,
            160,
            180,
            200,
            220,
            240,
            260,
            280,
            300,
            320,
            340,
            360,
            380,
            400,
            420,
            440,
            460,
            480,
            500,
            520,
            540,
            560,
            580,
            600,
            620,
            640,
            660,
            680,
            700,
            720,
            740,
            760,
            780,
            800,
            820,
            840,
            860,
            880,
            900,
            920,
            940,
            960,
            980,
        ]
    )
    is False
)
