def cost_ground_shipping(weight):
    cost = 0
    if weight <= 2.0:
        cost += 20 + 1.5 * (weight)
    elif weight > 2.0 and weight <= 6.0:
        cost += 20 + 3.00 * weight
    elif weight > 6.0 and weight <= 10.0:
        cost += 20 + 4.00 * weight
    elif weight > 10.0:
        cost += 20 + weight * 4.75
    premium_cost = cost + 105.00
    return cost


def cost_drone_shipping(weight):
    cost = 0
    if weight <= 2.0:
        cost += 4.5 * (weight)
    elif weight > 2.0 and weight <= 6.0:
        cost += 9.00 * weight
    elif weight > 6.0 and weight <= 10.0:
        cost += 12.00 * weight
    elif weight > 10.0:
        cost += weight * 14.25
    return cost


def best_option(weight):
    if cost_ground_shipping(weight) > cost_drone_shipping(weight):
        return "Drone shipping is the best option, costing you $" + str(cost_drone_shipping(weight))

    elif cost_ground_shipping(weight) == cost_drone_shipping(weight):
        return "They both cost the same at $" + str(cost_drone_shipping(weight))

    else:
        return "Ground shipping is the best option, costing you $" + str(cost_ground_shipping(weight))


print(best_option(4.8))