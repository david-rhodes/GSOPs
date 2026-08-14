# GSOPs: Where Magic Meets Reality
### Gaussian Splatting Operators for SideFX Houdini

[![GSOPs: Where Magic Meets Reality](/help/images/where_magic_meets_reality.jpg)](https://www.youtube.com/watch?v=d4F1cmAA_Ds)

[Sizzle Reel](https://youtu.be/-_gqsi6NYcY) | [Showcase](https://youtu.be/XZUUATb1u28)

## New in GSOPs 3.0
GSOPs 3.0 brings several new features and improvements. See the complete release notes [here](https://github.com/cgnomads/GSOPs/releases/tag/v3.0.0).

- Support for Houdini 22!
- Mip-splatting: Support for models trained with [mip-splatting](https://github.com/autonomousvision/mip-splatting) (antialiasing). Thanks to [Forian Hahlbohm](https://www.linkedin.com/in/florian-hahlbohm-a36b2b24a/) for his assistance!
- ML-Sharp: Import splats and generate cameras from Apple's [Sharp Monocular View Synthesis in Less Than a Second](https://github.com/apple/ml-sharp).
- `Gaussian Splats Bake`: Bake Gaussian splats to points, mesh, and density volumes. Great for voxelizing splats, converting to colored meshes, and simulating volumes.
- `Gaussian Splats Reduce`: Developed by [Bailey Tsang](https://www.linkedin.com/in/baileytsang/) and [Eyeline](https://eyelinestudios.com/), this [NanoGS](https://saliteta.github.io/NanoGS/)-inspired tool intelligently decimates Gaussian splat models. 
- `Gaussian Splats Relight IBL (3.0)`: Output irradiance (light emitting) and environment splats for compatibility with `Gaussian Splats Relight`.
- **[EARLY ACCESS]** `Gaussian Splats Relight`: Relight your splats with . . . splats!
- **[EARLY ACCESS]** `Gaussian Splats Light Emitter`: Turn splats into light emitters for `Gaussian Splats Relight`.

Additionally, the following [Early Access](https://github.com/cgnomads/GSOPs/wiki/Early-Access-Content) features have been promoted to the free tier:

- `Gaussian Splats Mirror`: Mirror Gaussian splats while preserving view-dependent effects (spherical harmonics).
- `Gaussian Splats Histogram`: Plot and edit splats in histogram space based on any floating point attribute (great for targeted adjustments and cleanup).
- `Gaussian Splats Sharpen`: Sharpen any Gaussian splat attribute, masked by any attribute.
- Viewport Renderer: Depth and World Position render modes.

## Recognition & Adoption
GSOPs won 3rd place in the [H20 SIDEFX LABS Tech Art Challenge](https://www.sidefx.com/community-main-menu/contests-jams/h20-tech-art-challenge/) and has since been used for the following projects:

- [Superman](https://www.youtube.com/watch?v=Pxd-q3ECBPs) (Framestore, 2025)
- [Dune: Prophecy](https://radiancefields.com/inside-rodeo-fx-s-use-of-gaussian-splatting-for-hbo-s-dune-prophecy) (Rodeo FX, 2025)
- A$AP Rocky's [HELICOPTER](https://www.youtube.com/watch?v=g1-46Nu3HxQ) (Grin Machine, 2026)
- [XA XÔI - MCK ft. OBITO](https://www.youtube.com/watch?v=NSkimwwZBRs) (Antiantiart, 2026)
- Death by Romy's [XR Concert](https://www.youtube.com/watch?v=j_I7ypiZGvM) (Prism AI, 2026)

## Where Magic Meets Reality
Add ✨ to your Gaussian splatting scenes with GSOPs — the most versatile Gaussian Splats editing toolset!

Gaussian splatting is a radiance field technology that turns photos and videos into high-quality 3D content with view-dependent effects and fast rendering. Gaussian Splatting Operators (GSOPs) is a plug-in for SideFX Houdini that grants artists total creative control over Gaussian splatting scenes.

GSOPs includes a real-time viewport renderer, [example files](https://github.com/cgnomads/GSOPs/tree/develop/hip), and a suite of digital assets for efficient import, editing, and export of 2D and 3D Gaussian splatting content.

Among its many capabilities, GSOPs is effective at isolating objects, eliminating noise and "floaters", deforming and animating splat models, composing scenes, meshing and relighting, performing feature analysis, and generating synthetic training data capable of delivering high-fidelity results with complex view-dependent effects.

Developed by [David Rhodes](https://www.linkedin.com/in/davidarhodes/) and [Ruben Diaz](https://www.linkedin.com/in/rubendz/), GSOPs is hosted under [CG Nomads](http://www.cgnomads.com).

Check out GSOPs on [LinkedIn](https://www.linkedin.com/feed/hashtag/?keywords=gsops) and [YouTube](https://www.youtube.com/playlist?list=PLh6-L_XjgKCv7PwEivhQJqEOCfqiY6pKg) for more examples.

💬 [Join us on Discord!](https://discord.gg/bwsvvRYNJa)

![GSplat Source](/help/images/gsplat_source_example.png)

## Motivation
Houdini's powerful, data-efficient architecture makes it the go-to platform for procedural content production across many industries. Its flexible and extensible design empowers users to tackle complex challenges at the right level of abstraction, focusing on problem-solving rather than low-level technicalities.

This unique combination of flexibility and ease of use is especially valuable in the rapidly evolving field of Novel View Synthesis. It enables quick prototyping, testing, and refinement of new workflows, keeping pace with the latest research. Additionally, it provides a direct path for innovations to transition into real-world applications within a well-established, production-ready solution.

SideFX, the developer of Houdini, fosters innovation through its "Labs" initiative. This incubator allows for the iteration of new tools and workflows before they become mainstream. Similarly, GSOPs provides a dedicated playground for Novel View Synthesis, enabling users to craft new workflows that closely align with the final visual result while prioritizing a creative and enjoyable process.

## Licensing
GSOPs began as free and open source software. As radiance field technologies evolve and gain traction across industries, we’re seeing increased demand for tools that empower artists, workflows that reduce iteration time, and pipelines that scale with production. GSOPs is our answer. 

Visit [cgnomads.com/licensing](https://www.cgnomads.com/licensing) or contact us at gsops.project@gmail.com for more information.

### Studios
Custom site licenses tailored to your studio’s needs. Support, source code, commercial usage, and Linux builds. 

### Schools
Free access for educators interested in incorporating GSOPs as part of their curriculum. 

Inagural Partners:
- [Stuttgart Media University](https://hdm-stuttgart.de/en/)
- [USC Ganek Immersive Studio](https://ganekimmersivestudio.com/)
- [UTS Animal Logic Academy](https://www.uts.edu.au/about/faculties/design-and-society/animal-logic-academy)

### Indies & Early Access
Get [Early Access](https://github.com/cgnomads/GSOPs/wiki/Early-Access-Content) to new GSOPs features and a "Supporter" Discord role. This is a great way to show your support and contribute to new feature development. 

We're passionate about the potential of editable radiance fields in SideFX Houdini and we're eager to continue pushing boundaries. If you believe in this initiative or have benefitted from GSOPs, please consider purchasing a license or making a donation. 

<a href="https://www.buymeacoffee.com/gsopsproject"><img src="help/images/support_gsops.png" alt="Support GSOPs" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Installation
Clone this repository (use the `develop` branch for the latest and greatest).
* **[Using Git CLI]** `git clone https://github.com/cgnomads/GSOPs`
* **[Using [GitHub Desktop](https://desktop.github.com/download/)]** Clone repository with URL: `https://github.com/cgnomads/GSOPs.git`
### Automatic
1. Install and configure the GSOPs Houdini package by opening the `hip/gsops_installer.hip` file in Houdini, selecting the `INSTALL_GSOPS` node and clicking `INSTALL`.
   
    <img width="548" alt="419229706-0c526dae-0ed9-4ab0-b986-9924f29c1481" src="https://github.com/user-attachments/assets/a0a08d0a-f6ea-491b-9419-a2e9e0fc706b" />
2. The installer will ask if you want to download sample data. Select "Yes" if you're interested in exploring our example content (recommended).
### Manual
1. Copy the `packages` directory from the cloned repo location to your Houdini user preferences directory. 
2. For each version of Houdini you want to use with GSOPs, change the "GSOPS" environment variable in the `.json` to your GSOPs clone location (e.g., `GSOPs_20.5.json`, `GSOPs_21.0.json`, or `GSOPs_22.0.json`). 
3. [Optional] Change the `GSOPS_USER_DATA_DIR` value as you see fit. This is where GSOPS configuration data will be stored--it needs to be a writeable location!
4. [Optional] Download sample data using the GSOPs shelf button.

### Early Access Supporters
Activate your license using the GSOPs shelf button.    

![GSOPs Shelf](/help/images/gsops_shelf.png)

## Getting Started
1. If you chose not to download sample data during installation, you should do that now via the GSOPs Shelf. 
2. Open a few example scenes from the `hip` directory. Use these to validate your installation and better understand Gaussian splatting workflows.
3. For the best experience, [disable OpenColorIO](https://vimeo.com/1001396463) and enable smooth shading in the viewport.
4. The `Gaussian Splats Source` SOP (i.e., the "render" node) does not currently have an output. This means it must exist at the end of your network.

## Notes
* Please be kind. We love innovating and learning, and we want you to benefit from this project.
* GSOPs is supported for Houdini 20.5 through Houdini 22.0. 
* Precompiled binaries are not available for Linux. See our [licensing options](https://www.cgnomads.com/licensing) for Studio Linux support. 
* Please adhere to the [SideFX Houdini License Agreement](https://www.sidefx.com/legal/license-agreement/).
* GSOPs can generate Gaussian splat training data, but it **cannot** train models. If you want to train models locally, please see [Lichtfeld Studio](https://lichtfeld.io/), [Postshot](https://www.jawset.com/), or [Brush](https://github.com/ArthurBrussee/brush) (a great option for Mac users).
* If you're interested in what you've seen and would like to discuss innovation/R&D collaboration opportunities, please [contact us](https://www.cgnomads.com/about-us).
* GSOPs is developed in our personal time and is provided as-is. 

## Features

### Digital Assets (Nodes)
<img src="/help/images/gsops_nodes.png" alt="drawing" width="300"/>

### Houdini 21+ Native Gaussian Splatting Interoperability
Houdini 21+ provides native Gaussian Splatting, but SideFX uses different attribute data conventions. Use the `Gaussian Splats Convert` SOP to toggle between GSOPs and Houdini's native conventions. 

### Coarse Meshing
GSOPs offers dependency-free coarse meshing for 3D Gaussian Splatting. Coarse meshes are an effective "sparse node graph" for splat editing operations. 

* [Coarse Meshing Utilities](https://github.com/cgnomads/GSOPs/wiki/GSOPs-Nodes#coarse-meshing)
* [Coarse Meshing Guidelines](https://github.com/cgnomads/GSOPs/wiki/Coarse-Meshing-Guidelines)

### Splat Animation Sequences
It's possible to create, import, edit, and export splat animation sequences (one .ply per file). You can load and render these in [Lichtfeld Studio](https://lichtfeld.io/), [Postshot](https://www.jawset.com/), [SuperSplat](https://playcanvas.com/supersplat/editor/), [Brush](https://github.com/ArthurBrussee/brush), and [Unity](https://github.com/cgnomads/GSOPs/blob/develop/extra/unity/UnityGaussianSplatting/INSTRUCTIONS.md).

### Synthetic Training Data
* You can use Houdini renders from procedural and manually generated camera poses (in COLMAP format) to convert your CG scenes to 3D Gaussian Splats. The `generate_training_data` SOP supports PNG image output, which enables the trainining of alpha-masked 3DGS models, which produces cleaner reconstructions.
* The `gaussian_splats_generate_training_data` SOP was updated in GSOPs 2.5 to support rendering in Karma and other 3rd party renderers. Previously, the render camera was constrained via Python, which caused evaluation issues in other Houdini contexts. The render camera is now constrained via channel expressions, avoiding this race condition. 

### Support for 2DGS
The `Gaussian Splats Import` SOP also accepts [2DGS](https://github.com/hbb1/2d-gaussian-splatting) models!

### [EARLY ACCESS] Support for Compressed Splats
In addition to `.ply`, import `.splat` and `.spz` file formats.

## Help
* Most digital assets exist in the SOPS context and (most) have their own help card documentation and parameter tooltips.
* Check the [wiki](https://github.com/cgnomads/GSOPs/wiki/GSOPs-Nodes).
* [Join us on Discord](https://discord.gg/bwsvvRYNJa).

## Acknowledgements
Supporters and Studio Licensees, thank you for your support! GSOPs 3.0 is dedicated to you!

### From David
[Jonne Geven](https://www.linkedin.com/in/jonne-geven/) and [Antti Veräjänkorva](https://www.linkedin.com/in/anttiv79/) have been my "rubber ducks." Thanks, guys. Always helpful to have cool people to bounce ideas around with.

[Aras Pranckevičius](https://aras-p.info) was quick to adopt Gaussian Splatting with a [Unity implementation](https://github.com/aras-p/UnityGaussianSplatting). He also went out of his way to help me with several problems I encountered during development. Thank you, Aras!

Major kudos to the original inventors of Gaussian Splatting, [Inria and the Max Planck Institut for Informatik (MPII)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)! 

### From Ruben 
I wouldn't have gotten this far without the inspiration from so many incredible open-source projects. While I haven’t directly reached out to the authors, their work has been immensely helpful, and I want to give special kudos to them:

- https://github.com/aras-p/UnityGaussianSplatting
- https://github.com/antimatter15/splat
- https://github.com/andrewwillmott/sh-lib

## Final Thoughts
This project is licensed under a _copyleft_ AGPL-3.0 license. If you require a different arrangement, please contact us to discuss alternatives.

If you create something cool and share it on social media, we'd love to see. Please consider tagging us!

**Keep splatting!** 
