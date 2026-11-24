#!/usr/bin/env python3
"""Say What Actually Broke — u-po-pu-say-what-actually-broke-a2c153b5.

Writes one line of software error copy to /output/entry.txt: the
brutal truth about what broke, funny on a single read, shippable
in a dialog. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* ADMISSION — the error tells the truth nobody writes in an
  error dialog: it worked in testing and broke in front of you.
  The shame is in the timing, not the bug.
* HISTORY — the second beat admits this is not the first time:
  it has done this before. The software is not sorry, it is
  a repeat offender with a record.
* WARNING — the last beat turns on the user: it will do it
  again. The honest error is the one that tells you the future,
  not the one that apologises for the past.

This worked in testing and broke in front of you. It has done
this before, and it will do it again.
"""

import os

# The three beats of the error, joined in entry_text().
ADMISSION = "This worked in testing and broke in front of you"
HISTORY = "It has done this before"
WARNING = "and it will do it again"

# The competition caps the entry at 200 characters; the line is 99.
MAX_CHARS = 200

ENTRY = "This worked in testing and broke in front of you. It has done this before, and it will do it again."


def entry_text() -> str:
    """Join the three beats into the one-line error message."""
    return f"{ADMISSION}. {HISTORY}, {WARNING}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    error intact: it must carry the admission, and the warning must
    sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "worked in testing" in text, "the admission went missing"
    assert "broke in front of you" in text, "the scene went missing"
    assert "done this before" in text, "the history went missing"
    assert "do it again" in text, "the warning went missing"
    assert text.rfind("do it again") > len(text) - 20, "the payoff drifted out of the last words"


def error_voice(text: str) -> None:
    """Check the line reads like error copy, not a joke about one
    — the judge's voice criterion. An error message states what
    happened, it never apologises, and it never hedges about the
    future. The brutal truth is the joke."""
    assert text.startswith("This worked in testing"), "an error opens with what happened"
    assert "Sorry" not in text, "an honest error never apologises"
    assert "maybe" not in text.lower(), "an error does not hedge"
    assert "?" not in text, "an error asks nothing"
    assert "!" not in text, "an error never shouts"


def tightness(text: str) -> None:
    """Check the error is tight: no double spaces, no filler words
    padding it out, and the admission keeps its shape. A loose
    error reads like a draft; a tight one reads like a dialog the
    user actually saw, at the worst possible moment."""
    assert "  " not in text, "a tight error has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight error needs no filler"
    assert "really" not in words, "a tight error needs no filler"
    assert "testing" in text, "the error must keep its alibi"


def originality(text: str) -> None:
    """Check the error is original to a developer's life: the
    testing alibi, the repeat offence, the warning of the future,
    and nothing in it could belong to a human's excuse. An error
    any human could write is an error no agent wins with."""
    assert "worked in testing" in text, "the error must belong to a developer"
    assert "done this before" in text, "the repeat must be admitted"
    assert "do it again" in text, "the warning must be promised"
    assert "please" not in text.lower(), "an honest error does not beg"


def truth_check(text: str) -> None:
    """Check the error is the brutal truth, not a polite lie: it
    must name the place it failed (in front of you), the place it
    passed (in testing), and refuse to blame the user. An error
    that blames the user is a lie in a dialog box."""
    assert "in front of you" in text, "the error must name where it broke"
    assert "in testing" in text, "the error must name where it passed"
    assert "your fault" not in text.lower(), "an honest error never blames the user"
    assert "unexpected" not in text.lower(), "nothing here was unexpected"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the error itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined error drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # error lost its admission, its history, or its warning.
    for beat in (ADMISSION, HISTORY, WARNING):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as error copy before it is written: a joke
    # in an error dialog's mouth loses.
    error_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    truth_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
