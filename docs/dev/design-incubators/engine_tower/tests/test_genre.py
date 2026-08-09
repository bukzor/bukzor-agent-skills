from engine_tower.genre import restrict
from engine_tower.standing import OBLIGATED, STIPULATED, Evidence, certified, standing

CORE_ENTRIES = frozenset({"m", "g"})
CORE_EV = frozenset(
    {Evidence("m", STIPULATED), Evidence("g", STIPULATED, frozenset({"m"}))}
)
CORE = standing(CORE_EV, CORE_ENTRIES)
EXT_ENTRIES = CORE_ENTRIES | {"r1"}


def test_a_confined_extension_conserves_core_standing():  # CONSERVE, SATISFACTION, FREE_CONSERVE
    # concludes only on its own entries, citing core entries as premises freely
    ext_ev = CORE_EV | {Evidence("r1", OBLIGATED, frozenset({"g"}))}
    ext = standing(ext_ev, EXT_ENTRIES)
    assert restrict(ext, CORE_ENTRIES) == CORE


def test_an_unconfined_extension_breaks_conservation():  # SATISFACTION
    # the extension concludes on a core entry
    rogue_ev = CORE_EV | {Evidence("g", certified("rogue-check"))}
    rogue = standing(rogue_ev, EXT_ENTRIES)
    assert restrict(rogue, CORE_ENTRIES) != CORE
