from src.analyze_log import best_seller, never_requested, day_never_used


class TrackOrders:
    def __init__(self):
        self._data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        return self._data.append(
            {"cliente": customer, "pedido": order, "dia": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        return best_seller(self._data, customer)

    def get_never_ordered_per_customer(self, customer):
        return never_requested(self._data, customer)

    def get_days_never_visited_per_customer(self, customer):
        return day_never_used(self._data, customer)

    def get_busiest_day(self):
        allDays = {}
        busiest_day = self._data[0]["dia"]

        for sale in self._data:
            if sale["dia"] not in allDays:
                allDays[sale["dia"]] = 1
            else:
                allDays[sale["dia"]] += 1
            if allDays[sale["dia"]] > allDays[busiest_day]:
                busiest_day = sale["dia"]
        return busiest_day

    def get_least_busy_day(self):
        allDays = {}
        busiest_day = self._data[0]["dia"]

        for sale in self._data:
            if sale["dia"] not in allDays:
                allDays[sale["dia"]] = 1
            else:
                allDays[sale["dia"]] += 1
            if allDays[sale["dia"]] < allDays[busiest_day]:
                busiest_day = sale["dia"]
        return busiest_day
