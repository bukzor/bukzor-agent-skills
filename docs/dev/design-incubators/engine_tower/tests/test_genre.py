from engine_tower.genre import confined, restrict
from engine_tower.standing import OBLIGATED, STIPULATED, Evidence, certified, standing

CORE_ENTRIES = frozenset({"m", "g"})
CORE_EV = frozenset(
    {Evidence("m", STIPULATED), Evidence("g", STIPULATED, frozenset({"m"}))}
)
CORE = standing(CORE_EV, CORE_ENTRIES)
OWN_ENTRIES = frozenset({"r1"})
EXT_ENTRIES = CORE_ENTRIES | OWN_ENTRIES


def test_a_confined_extension_conserves_core_standing():  # CONFINE, CONSERVE, SATISFACTION, FREE_CONSERVE
    # concludes only on its own entries, citing core entries as premises freely
    ext_ev = CORE_EV | {Evidence("r1", OBLIGATED, frozenset({"g"}))}
    assert confined(ext_ev - CORE_EV, OWN_ENTRIES)  # the hypothesis, checked
    ext = standing(ext_ev, EXT_ENTRIES)
    assert restrict(ext, CORE_ENTRIES) == CORE


def test_an_unconfined_extension_breaks_conservation():  # CONFINE, SATISFACTION
    # the extension concludes on a core entry
    rogue_ev = CORE_EV | {Evidence("g", certified("rogue-check"))}
    assert not confined(rogue_ev - CORE_EV, OWN_ENTRIES)
    rogue = standing(rogue_ev, EXT_ENTRIES)
    assert restrict(rogue, CORE_ENTRIES) != CORE
