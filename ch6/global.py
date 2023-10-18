def max_promo(x, y):
    return max(x, y)
def min_promo(x, y):
    return min(x, y)

def best_promo(x, y):
    return max([promo(x, y) for promo in promos])

promos = [globals()[name] for name in globals() if name.endswith("promo") and name != 'best_promo']
import pdb;pdb.set_trace()