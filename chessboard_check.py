def isValidChessBoard(board):
    """A simple program that checks whether or nor a given board is valid."""

    # Generate valid positions in '1a' to '8h' format
    validPositions = [str(row) + col for row in range(1, 9) for col in 'abcdefgh']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    wPieces = [v for v in board.values() if v.startswith('w')]
    bPieces = [v for v in board.values() if v.startswith('b')]
    allPieces = list(board.values())

    # Check 1: Exactly one black king and one white king.
    if bPieces.count('bking') != 1 or wPieces.count('wking') != 1:
        return False

    # Check 2: Each player must have at most 16 pieces.
    if len(bPieces) > 16 or len(wPieces) > 16:
        return False

    # Check 3: At most 8 pawns for each player.
    if bPieces.count('bpawn') > 8 or wPieces.count('wpawn') > 8:
        return False

    # Check 4: All pieces must be on a valid space from '1a' to '8h'.
    for k in board.keys():
        if k not in validPositions:
            return False

    # Check 5: The pieces must begin with either a 'w' or 'b' and be a valid piece name.
    for v in allPieces:
        if len(v) < 2 or v[0] not in ('w', 'b'):
            return False
        if v[1:] not in pieces:
            return False

    return True
