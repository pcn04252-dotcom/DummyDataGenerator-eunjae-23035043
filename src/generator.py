import random

_NAME_PREFIXES = ["실리콘 웨이퍼", "GaN 에피택셜", "SiC 파워기판", "포토레지스트", "산화막 웨이퍼"]
_NAME_SUFFIXES = ["4인치", "6인치", "8인치", "12인치", "PR7", "SiO2"]


def generate_items(
    count: int, rng: random.Random | None = None
) -> list[tuple[str, int]]:
    if count < 0:
        raise ValueError("count는 0 이상이어야 합니다.")

    rng = rng or random.Random()
    items = []
    for _ in range(count):
        name = f"{rng.choice(_NAME_PREFIXES)}-{rng.choice(_NAME_SUFFIXES)}"
        quantity = rng.randint(1, 500)
        items.append((name, quantity))
    return items
