# dictionary for the blocks including name and cells
shapes = [ 
    {
        "name": "1x1",
        "cells": [(0, 0)]
    },
    {
        "name": "2x1",
        "cells": [(0, 0), (1, 0)]
    },
    {
        "name": "2x2",
        "cells": [(0, 0), (1, 0), (0, 1), (1, 1)]
    },
    {
        "name": "3x1",
        "cells": [(-1, 0), (0, 0), (1, 0)]
    },
    {
        "name": "top left corner",
        "cells": [(0, 1), (0, 0), (1, 0)]
    },
    {
        "name": "top right corner",
        "cells": [(-1, 0), (0, 0), (0, -1)]
    },
    {
        "name": "t",
        "cells": [(-1, 0), (0, 0), (1, 0), (0, -1)]
    },
    {
        "name": "t inverted",
        "cells": [(-1, 0), (0, 0), (1, 0), (0, 1)]
    }
]

piece_colours = [
    "#FF6B6B",
    "#4ECDC4",
    "#45B7D1",  
    "#96CEB4",  
    "#FFEAA7",  
    "#DDA0DD",
    "#98D8C8",
    "#F7DC6F",
    "#BB8FCE",
    "#85C1E9",
]