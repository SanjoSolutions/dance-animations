import type { DanceAnimation } from './catalog.ts';
import type { Performer } from './clip-binding.ts';

export interface DanceMove {
  id: string;
  label: string;
  solo: boolean;
  variants: DanceAnimation[];
}

/** Group the two authored character versions of a move into one UI choice. */
export function retrieveMoves(entries: DanceAnimation[], style: string): DanceMove[] {
  const groups = new Map<string, DanceMove>();
  for (const entry of entries.filter(entry => entry.style === style)) {
    let name = entry.id;
    let actorRemoved = /^(man|woman)_/.test(name);
    name = name.replace(/^(man|woman)_/, '');
    const prefix = (style === 'house_dance' ? ['house_dance', 'house'] : [style])
      .find(prefix => name === prefix || name.startsWith(`${prefix}_`) || name.startsWith(`solo_${prefix}_`));
    if (prefix) {
      if (name === prefix) name = 'routine';
      else if (name.startsWith(`${prefix}_`)) name = name.slice(prefix.length + 1);
      else name = name.slice(prefix.length + 6);
    }
    if (/^(man|woman)_/.test(name)) {
      actorRemoved = true;
      name = name.replace(/^(man|woman)_/, '');
    }
    if (!actorRemoved) name = name.replace(/_(man|woman)$/, '');
    if (name === 'man' || name === 'woman') name = 'routine';
    const solo = entry.performers.length === 1;
    const id = solo ? name : `${name}:partners`;
    const group = groups.get(id) ?? {
      id, label: name.replaceAll('_', ' ').replace(/^./, letter => letter.toUpperCase()), solo, variants: [],
    };
    group.variants.push(entry);
    groups.set(id, group);
  }
  const moves = [...groups.values()];
  for (const move of moves) {
    if (!move.solo && moves.some(other => other.solo && other.label === move.label)) move.label += ' (Partners)';
  }
  return moves.sort((a, b) => a.label.localeCompare(b.label));
}

export function retrieveVariant(move: DanceMove, character: Performer): DanceAnimation {
  return move.variants.find(entry => entry.performers.length === 1 && entry.performers[0] === character) ?? move.variants[0];
}
