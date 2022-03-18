class RankValidator():
    def _ranks_with_count(self, count):
        # uses dictionary comprehension to get
        # dict containing the rank
        # and the number of times that rank
        # appears in the Hand
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}

        for card in self.cards:
            # handles if no entry in dict yet.
            # Makes dict entry for each rank.
            card_rank_counts.setdefault(card.rank, 0)

            # increment dict entry by 1.
            card_rank_counts[card.rank] += 1
        
        return card_rank_counts