def calculate_budget(
    total_budget,
    flight_cost,
    hotel_cost,
    food_cost,
    transport_cost,
    activities_cost
):
    """
    Calculate total travel expenses and remaining budget.
    """

    total_expense = (
        flight_cost
        + hotel_cost
        + food_cost
        + transport_cost
        + activities_cost
    )

    remaining_budget = total_budget - total_expense

    return {
        "total_budget": total_budget,
        "total_expense": total_expense,
        "remaining_budget": remaining_budget
    }



if __name__ == "__main__":
    result = calculate_budget(
        15000,
        5000,
        3000,
        2000,
        1000,
        1500
    )

    print(result)