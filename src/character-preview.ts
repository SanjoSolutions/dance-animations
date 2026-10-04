import { Object3D } from 'three';
import { clone } from 'three/addons/utils/SkeletonUtils.js';

/** Rotation is the preview heading around the vertical axis, in radians. */
export function createCharacterPreview(template: Object3D, rotation = 0): Object3D {
  const model = clone(template);
  model.rotation.y += rotation;
  return model;
}
