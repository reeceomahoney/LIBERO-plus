# This is an example script to get all the affordance information specified in xml files.

import init_path
from libero_plus.libero_plus.envs.objects import OBJECTS_DICT
from libero_plus.libero_plus.utils.object_utils import get_affordance_regions

affordances = get_affordance_regions(OBJECTS_DICT)

print(affordances)
