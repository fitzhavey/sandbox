# A-Frame: Tap to Place Ground

## Notes:
- currently doesn't work in browser :(

This example allows the user to grow cacti 🌵 by tapping or clicking the ground. Showcases raycasting, spawning new objects, and importing a 3D model.

![example usage](https://media1.giphy.com/media/rAi32DNlsWNpItOpDr/giphy.gif?cid=790b76117e57cc8f6477a68ecd7cd4f8f2d3a350a8e5e2fa&rid=giphy.gif&ct=g)


Optimizing for Metaversal Deployment
With R18, the all-new 8th Wall Engine features Metaversal Deployment, enabling you to create WebAR experiences once and deploy them to smartphones, tablets, computers and both AR and VR headsets. This project has a few platform-specific customizations:

In body.html, we add the "allowedDevices: any" parameter to our xrweb component in <a-scene> which ensures the project opens on all platforms, including desktop. Environment parameters have been customized to generate an open desert space.

About World Tracking
Built entirely using standards-compliant JavaScript and WebGL, 8th Wall’s Simultaneous Localization and Mapping (SLAM) engine is hyper-optimized for real-time AR on mobile browsers. Features include Six Degrees of Freedom (6-DoF), Lighting estimation, instant surface detection and responsive scale.

The Y position of the camera at start effectively determines the scale of virtual content on a surface (e.g. smaller y, bigger content). This can be reset at any time by calling recenter().

The camera should NOT be at a height (Y) of zero. It must be set to a non-zero value.

Attribution
Toon Cactus by PolyChromic