import type { DanceCatalog } from './catalog';
import type { Performer } from './clip-binding';

export function retrieveCharacterFile(catalog: DanceCatalog, style: string, actor: Performer): string {
  const wardrobe = catalog.wardrobe;
  const profile = wardrobe && (Object.values(wardrobe.profiles).find(profile => profile.styles.includes(style))
    ?? wardrobe.profiles[wardrobe.default]);
  return profile?.models[actor].file ?? catalog.models[actor].file;
}
