export interface DanceAnimation {
  id: string;
  style: string;
  label: string;
  performers: ('man' | 'woman')[];
  duration: number;
  file: string;
  transportFile?: string;
  /** Preview heading around the vertical axis, in radians. */
  previewRotation?: number;
  sourceFile: string | null;
  animationName: string;
  status: string;
  /** Directed transitions hold their final pose after one playback. */
  loop?: boolean;
}

export interface DanceCatalog {
  models: Record<'man' | 'woman', { file: string }>;
  props?: Record<string, { file: string; styles: string[] }>;
  wardrobe?: {
    default: string;
    profiles: Record<string, { label: string; styles: string[]; models: Record<'man' | 'woman', { file: string }> }>;
  };
  styles: { id: string; label: string; playable: number; sources: number }[];
  animations: DanceAnimation[];
  sourceCount: number;
  sourceOnlyCount: number;
}

export function assetUrl(path: string): string {
  return new URL(import.meta.env.BASE_URL + path, document.baseURI).href;
}
