// Copyright (c) 2021 8th Wall, Inc.
/* globals AFRAME */

AFRAME.registerComponent('shoot-airplane', {
	init() {
	  const camera = document.getElementById('camera')
	  const splatSnd = document.querySelector('#splat').components.sound

	  this.el.sceneEl.addEventListener('touchstart', (event) => {
		// Create element to be thrown, setting position, scale, and model
		const airplane = document.createElement('a-entity')
		airplane.setAttribute('position', camera.object3D.position)
		airplane.setAttribute('scale', '0.35 0.35 0.35')
		airplane.setAttribute('gltf-model', '#airplaneModel')

		// Choose a random rotation offset for some variation
		// const randos

		// Set velocity, rotated with camera direction
		const velocity = new THREE.Vector3(0, 0, -100)
		velocity.applyQuaternion(camera.object3D.quaternion)
		airplane.setAttribute('velocity', velocity)

		// Add physics body
		airplane.setAttribute('body', {
		  type: 'dynamic',
		  sphereRadius: 0.035,
		  shape: 'sphere',
		})

		airplane.setAttribute('shadow', {
		  receive: false,
		})

		// Add airplane to scene
		this.el.sceneEl.appendChild(airplane)

		// The splat is created at the same time as the thrown airplane so
		// there is time to load the model before it hits the ground
		const splatBase = document.createElement('a-entity')
		splatBase.setAttribute('visible', 'false')

		// The splat consists of a model wrapped in an empty
		// parent so we can apply the correct scaling animation
		const splat = document.createElement('a-entity')
		splat.setAttribute('gltf-model', '#airplaneModel')
		splat.setAttribute('scale', '1 1 1')
		splatBase.appendChild(splat)

		this.el.sceneEl.appendChild(splatBase)

		let didCollide = false
		airplane.addEventListener('collide', (e) => {
		  // Only want to do the splat once, and with the ground only
		  if (didCollide || e.detail.body.el.id !== 'ground') {
			return
		  }
		  didCollide = true

		  // Stop previous splat sound
		  splatSnd.stopSound()
		  // Play splat sound
		  splatSnd.playSound()

		  // Copy positioning of thrown airplane to splat
		  splatBase.object3D.position.copy(airplane.object3D.position)
		  splat.object3D.rotation.copy(airplane.object3D.rotation)

		  splatBase.object3D.visible = true

		  airplane.setAttribute('visible', 'false')

		  // We can't remove the thrown airplane until the physics step is over
		  setTimeout(() => {
			airplane.parentNode.removeChild(airplane)
		  }, 0)

		  // Using animation component to show flattening
		  splatBase.setAttribute('animation__scale', {
			property: 'scale',
			from: '1 1 1',
			to: '3 0.1 3',
			dur: 500,
			easing: 'easeOutQuad',
		  })

		  // After 2.5 seconds, shrink the splat away and delete it
		  setTimeout(() => {
			splatBase.setAttribute('animation__scale', {
			  property: 'scale',
			  from: '3 0.1 3',
			  to: '0.001 0.001 0.001',
			  dur: 1500,
			  easing: 'easeInQuad',
			})
			setTimeout(() => splatBase.parentNode.removeChild(splatBase), 1500)
		  }, 2500)
		})
	  })
	},
  })