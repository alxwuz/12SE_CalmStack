class Blocks:
    def __init__(self, name, colour, cells):
        self._name = name
        self._colour = colour
        self._cells = list(cells)

        def get_name(self):
            return self._name
        
        def get_colour(self):
            return self._colour

        def get_cells(self):
            return list(self._cells)
        
    def blockShapes(self):
        shapes = [
            {
                "name": "1x1",
                "colour": "empty",
                "cells": [(0, 0)]
            },
            {
                "name": "2x1",
                "colour": "empty",
                "cells": [(0, 0), (1, 0)]
            },
            {
                "name": "2x2",
                "colour": "empty",
                "cells": [(0, 0), (1, 0) (0,1) (1, 1)]
            },
            {
                "name": "3x1",
                "colour": "empty",
                "cells": [(-1, 0), (0, 0), (1, 0)]
            },
            {
                "name": "top left corner",
                "colour": "empty",
                "cells": [(0, 0), (0, 1), (1, 1)]
            },
            {
                "name": "top right corner",
                "colour": "empty",
                "cells": [(-1, 0), (0, 0), (0, -1)]
            },
            {
                "name": "t",
                "colour": "empty",
                "cells": [(-1, 0), (0, 0), (1, 0), (0, -1)]
            },
            {
                "name": "t inverted",
                "colour": "empty",
                "cells": [(-1, 0), (0, 0), (1, 0), (0, 1)]
            }
            ]

            



