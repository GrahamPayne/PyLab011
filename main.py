#!/usr/bin/env python3

from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite


def build_mindmap():
    # Root of the mind map
    root = MindMapComposite("Tidal → Pure Data Song", "circle")

    # 1. Environment setup
    env = MindMapComposite("Environment Setup", "oval")
    env.add(MindMapLeaf("Install TidalCycles", "plain"))
    env.add(MindMapLeaf("Install SuperDirt", "plain"))
    env.add(MindMapLeaf("Install Pure Data (Pd)", "plain"))
    env.add(MindMapLeaf("Check audio interface works", "plain"))
    root.add(env)

    # 2. MIDI / audio routing
    routing = MindMapComposite("MIDI / Audio Routing", "square")
    routing.add(MindMapLeaf("Send MIDI from Tidal", "plain"))
    routing.add(MindMapLeaf("Choose a virtual MIDI port", "plain"))
    routing.add(MindMapLeaf("Receive MIDI in Pd", "plain"))
    routing.add(MindMapLeaf("Map MIDI notes to Pd synths", "plain"))
    routing.add(MindMapLeaf("Test a simple loop", "plain"))
    root.add(routing)

    # 3. Pure Data patch design
    pd_patch = MindMapComposite("Pure Data Patch Design", "cloud")
    pd_patch.add(MindMapLeaf("Drum synth (kick, snare, hat)", "plain"))
    pd_patch.add(MindMapLeaf("Bass synth with filter sweep", "plain"))
    pd_patch.add(MindMapLeaf("FX sends: reverb / delay", "plain"))
    pd_patch.add(MindMapLeaf("Master volume / limiter", "plain"))
    root.add(pd_patch)

    # 4. Song structure
    song = MindMapComposite("Song Structure", "hexagon")
    song.add(MindMapLeaf("Intro: simple, low density", "plain"))
    song.add(MindMapLeaf("Main groove: full drums + bass", "plain"))
    song.add(MindMapLeaf("Break: remove kick, add texture", "plain"))
    song.add(MindMapLeaf("Build: more density / FX", "plain"))
    song.add(MindMapLeaf("Outro: fade back to intro idea", "plain"))
    root.add(song)

    # 5. Recording and export
    record = MindMapComposite("Recording & Export", "bang")
    record.add(MindMapLeaf("Route Pd audio to DAW / Audacity", "plain"))
    record.add(MindMapLeaf("Set levels, avoid clipping", "plain"))
    record.add(MindMapLeaf("Record live performance", "plain"))
    record.add(MindMapLeaf("Export final WAV / MP3", "plain"))
    root.add(record)

    return root


def main():
    # Mermaid mindmap syntax starts with the word 'mindmap'
    print("mindmap")

    # Root line uses 'root' before the node text
    root = build_mindmap()
    print("  root{}".format(str(root)))

    # Then print all children under the root, indented
    for child in root.children:
        child.display(4)


if __name__ == "__main__":
    main()
