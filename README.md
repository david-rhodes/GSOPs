# GSOPs (Gaussian Splat Operators) for SideFX Houdini

[![Watch the video](https://img.youtube.com/vi/CNo7H39OaE8/hqdefault.jpg)](https://www.youtube.com/embed/CNo7H39OaE8)  
[Watch the video](https://www.youtube.com/embed/CNo7H39OaE8)

## About
Use GSOPs to import, edit, and export gaussian splat models, or generate synthetic training data. Synthetic data is capable of producing high-fidelity models with view-dependent effects, relatively small file sizes, and incredible rendering performance on most modern devices.

With GSOPs, you can isolate objects or sections, eliminate noise and floaters, deform and animate models, compose scenes, mesh splats, and conduct feature analysis.

<img src="https://raw.githubusercontent.com/david-rhodes/GSOPs/develop/help/images/feature_analysis.png" title="Gaussian Splatting feature analysis comparison." alt="Gaussian Splat feature analysis comparison." width="800" height="800">

The following SOP nodes are provided:
* `gaussian_splats_align_by_points`: Aligns a gaussian splat model to the world origin.
* `gaussian_splats_crop`: Crops or groups a splat model.
* `gaussian_splats_dbscan`: Density-based spatial clustering useful for removing noise and outliers.
* `gaussian_splats_deform`: Deform splat models using polygonal geometry.
* `gaussian_splats_export`: Exports Houdini gaussian splat geometry to disk, converting all relevant point data to native gaussian splat attributes in the process.
* `gaussian_splats_feature_analysis`: Perform statistical analysis of gaussian splat models.
* `gaussian_splats_generate_training_data`: Generate synthetic data suitable for training gaussian splat models.
* `gaussian_splats_import`: Loads a trained gaussian splat model, converting all relevant data to native Houdini point attributes.
* `gaussian_splats_import_cameras`: Imports the cameras.json file generated as a result of training gaussian splat models.
* `gaussian_splats_visualize_boxes`: Visualize gaussian splats as opaque boxes.

For more information, please reference the built-in help cards. *(SideFX, if you are reading this, thank you for making an incredible documentation system!)*

## Notes
* Please be kind. GSOPs was developed as a side project. I love innovating and learning, and I want you to benefit from this project.
* All digital assets and example scenes are under the Houdini Apprentice license. I have submitted GSOPs to the [H20 SIDEFX LABS Tech Art Challenge](https://www.sidefx.com/community-main-menu/contests-jams/h20-tech-art-challenge/). If GSOPs win, I'll kindly ask SideFX for a project-wide license upgrade. In the meantime, feel free to experiment with GSOPs in Houdini Apprentice, or use it for your own education. Please adhere to the [SideFX Houdini License Agreement](https://www.sidefx.com/legal/license-agreement/).
* GSOPs does not currently include a viewport renderer, but one is in progress.
* GSOPs can generate gaussian splat training data, but it cannot train models. If you want to train models locally, please see [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://github.com/graphdeco-inria/gaussian-splatting).
* Credit or acknowledgement when sharing cool stuff made with GSOPs is appreciated. Feel free to tag [David Rhodes](https://www.linkedin.com/in/davidarhodes/).
* If you're interested in what you've seen and would like to discuss short-term innovation/R&D collaboration opportunities, please contact me: david.a.rhodes.3d@gmail.com.

## Installation
1. Clone this repository.
2. Copy the GSOPs.json file found in the repository root, and paste it in the $HOUDINI_USER_PREF_DIR/packages/ folder. You may need to create this folder.
3. Edit the GSOPs.json file you just pasted, and modify the $GSOPS path found inside to the the location used in step one.

## Help
* All digital assets exist in the SOPS context and (most) have their own help card documentation.
* Examples scenes and content exist in the `hip` directory. Use these to understand gaussian splat workflows.
* For demonstrations of what GSOPs are capable of, please see [GSOPS on LinkedIn](https://www.linkedin.com/feed/hashtag/?keywords=gsops).
* Houdini provides many wonderful tools that will help you work with Gaussian Splat data. If you're not already familiar, check out the following SOP nodes: point cloud normal/surface, VDB from particles/polygons, cluster, and group (w/keep in bounding regions).

## Known Issues
I consider GSOPs to be a professional-grade prototyping toolset. It is not free from error, and the user experience could be improved in many areas. Here are some of the known issues:
* Rotating a splat model will not update spherical harmonics data accordingly. As a result, view-dependent lighting effects will not behave correctly in exported models.
* Scaling a splat model will not scale individual splats, leading to visible artifacts in exported models.
* Rendering the viewport with `gaussian_splats_generate_training_data` will always use the viewport aspect ratio as the camera resolution aspect ratio (with a maxmium dominant resolution of 720 in Houdini Apprentice). This is because I could not find a python hook to set the viewport size. As a workaround, be sure to set your viewport size manually before performing viewport renders.
* It is possible to create bad export data when using the `unpack` feature of `gaussian_splats_visualize_boxes`. As a workaround, simply avoid having this node in any data stream leading to an export node.
* The`gaussian_splats_feature_analysis visualizer` sometimes fails to refresh (toggle the visualize button as a workaround), and this sometimes  precedes as Houdini crash. The UX when dealing with very small or large attribute values needs improvement.
* View-dependent lighting effects (i.e., spherical harmonics) can only be previewed with the "Toy" operator: `gaussian_splats_evaluate_spherical_harmonics`. This node is not yet documented, but it's available if you're feeling brave.
* There's quite a bit of python in the project which needs additional error handling.
* I briefly tested GSOPs on OSX, but it was developed on Windows. Please report bugs.
   
## Contribution Wish List
I have not been able to implement all the cool ideas I have. However, my goal in open-sourcing GSOPs is to involve the community. After all, we're stronger together!

Here's my personal wish list for community contributions (but feel free to bring your own innovations to this project):
- [ ] Viewport Renderer (WIP--likely using [glsl](https://www.sidefx.com/docs/houdini/shade/glsl.html)).
- [ ] Karma/LOPS render support (this has been requested by a few people already).
- [ ] [Segment Any 3D GAussians (SAGA)](https://github.com/Jumpat/SegAnyGAussians) or similar segmentation integration.
- [ ] Custom python viewer states + "magic wand" functionality (e.g., spatial-aware selection according to attribute similarity).
- [ ] PDG/TOPS support for batching and automation (probably to generate synthetic training data with `gaussian_splats_generate_training_data`).
- [ ] Improved camera coverage generator for `gaussian_splats_generate_training_data`. My first-pass (object-centric) implementation is somewhat naive. It would also be great to have a camera coverage solver for environments.
- [ ] Icons (I borrowed the best-match icons I could find from SideFX, but custom icons would be great).
- [ ] Promotional material (graphic design or other content you make using GSOPs).
- [ ] I/O for compressed splats. There's no standardized compression format for 3DGS yet. However, [PlayCanvas' SuperSplat compressed.ply format](https://blog.playcanvas.com/compressing-gaussian-splats/) provides a good balance of simplicity and compression rates. The [discussion](https://github.com/mkkellogg/GaussianSplats3D/issues/47) around standardizing compressed 3DGS has stalled, but maybe you can help breathe life into it!

## Acknowledgements
[Jonne Geven](https://www.linkedin.com/in/jonne-geven/) and [Antti Veräjänkorva](https://www.linkedin.com/in/anttiv79/) have been my "rubber ducks." Thanks, guys. Always helpful to have cool people to bounce ideas around with.

[Aras Pranckevičius](https://aras-p.info) was quick to adopt Gaussian Splatting with a [Unity implementation](https://github.com/aras-p/UnityGaussianSplatting). He also went out of his way to help me with several problems I encountered during development. Thank you, Aras!

Major kudos to the original inventors of Gaussian Splatting, [Inria and the Max Planck Institut for Informatik (MPII)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)! 

Finally, thank you, community! Your support, interest, and rapid contributions to gaussian splatting have inspired and motivated me. 

Enjoy!
