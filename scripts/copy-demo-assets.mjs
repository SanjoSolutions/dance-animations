import { cp, mkdir, readFile, writeFile } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';
import { dirname } from 'node:path';
import catalog from '../catalog.json' with { type: 'json' };
import music from '../music.json' with { type: 'json' };

await mkdir('dist/animations', { recursive: true });
await cp('models', 'dist/models', { recursive: true });
await mkdir('dist/assets/music', { recursive: true });
for (const file of new Set(music.tracks.map(track => track.file))) {
  await cp(file, `dist/${file}`);
}
await cp('assets/music/selections.json', 'dist/assets/music/selections.json');
await cp('music.json', 'dist/music.json');
// Pages serves runtime assets only. Editable Blender sources remain in Git.
for (const entry of catalog.animations) {
  if (entry.file) {
    entry.transportFile = `${entry.file}.gz`;
    await mkdir(dirname(`dist/${entry.transportFile}`), { recursive: true });
    await writeFile(`dist/${entry.transportFile}`, gzipSync(await readFile(entry.file), { level: 9 }));
  }
}
await writeFile('dist/catalog.json', JSON.stringify(catalog));
console.log(`Packaged ${catalog.animations.filter(entry => entry.file).length} runtime clips.`);
