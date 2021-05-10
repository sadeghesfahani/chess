possible_pawn_list = list()
        forward = True
        if self.white:
            if self.first_move:
                for r in range(1, 3):
                    if board_column.find(self.location[0]) + r < 8 and forward:
                        if main_board.board_data[f"{self.location[0]}{int(self.location[1]) + r}"][1] is None:
                            possible_pawn_list.append(f"{self.location[0]}{int(self.location[1]) + r}")
                        else:
                            forward=False
                if board_column.find(self.location[0]) + 1 < 8:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                if board_column.find(self.location[0]) - 1 >= 0:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
            else:

                if main_board.board_data[f"{self.location[0]}{int(self.location[1]) + 1}"][1] is None:
                    possible_pawn_list.append(f"{self.location[0]}{int(self.location[1]) + 1}")

                if board_column.find(self.location[0]) + 1 <= 8:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                if board_column.find(self.location[0]) - 1 >= 0:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
        else:
            if self.first_move:
                if forward:
                    for r in range(1, 3):
                        if main_board.board_data[f"{self.location[0]}{int(self.location[1]) - r}"][1] is None:
                            possible_pawn_list.append(f"{self.location[0]}{int(self.location[1]) - r}")
                        else:
                            forward = False
                if board_column.find(self.location[0]) - 1 >= 0:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) - 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) - 1}")
                if board_column.find(self.location[0]) - 1 >= 0:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}")
            else:

                if main_board.board_data[f"{self.location[0]}{int(self.location[1]) - 1}"][1] is None:
                    possible_pawn_list.append(f"{self.location[0]}{int(self.location[1]) - 1}")

                if board_column.find(self.location[0]) + 1 <= 8:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) - 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) - 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) + 1]}{int(self.location[1]) - 1}")
                if board_column.find(self.location[0]) - 1 >= 0:
                    if main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}"][
                        1] is None:
                        pass
                        # possible_pawn_list.append(
                        # f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) + 1}")
                    elif main_board.board_data[
                        f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}"][
                        1].white is not self.white:
                        possible_pawn_list.append(
                            f"{board_column[board_column.find(self.location[0]) - 1]}{int(self.location[1]) - 1}")
        return possible_pawn_list