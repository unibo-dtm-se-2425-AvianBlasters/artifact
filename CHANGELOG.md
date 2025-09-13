## [3.1.0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/compare/3.0.0...3.1.0) (2025-09-13)


### Features

* updated name of constant to fit better with its actual use ([62403c7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/62403c7357322663715e04778081fcd94c348138))


### Refactoring

* **controller:** update to the graphical refresh logic linked to fps ([55942a4](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/55942a45e1422f7133bfcff97113267c49051375))

## [3.0.0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/compare/2.0.0...3.0.0) (2025-09-12)


### ⚠ BREAKING CHANGES

* made so try_attack has a parameter of type Character in attack_handler adjacent classes

### Bug Fixes

* made so try_attack has a parameter of type Character in attack_handler adjacent classes ([2077910](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2077910bc66204fa7c89495db873719447cd8cda))

## [2.0.0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/compare/1.0.0...2.0.0) (2025-09-12)


### ⚠ BREAKING CHANGES

* moved menu adjacent classes into a package of their own

### Bug Fixes

* moved menu adjacent classes into a package of their own ([56bd563](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/56bd563afd7f82c387202724a2830cd6b6a83a37))


### Build and continuous integration

* updated url in setup.py ([22d63b8](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/22d63b82c105429a8cbe8279f7fd807256099f5a))


### General maintenance

* reinstaintated default MyClass ([0b331d6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0b331d6a66529454e9ce494bb530515e90acb425))
* removed unused default package classes ([6de59f5](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/6de59f51d16dd0f5eb767e3dd2a525dd15575474))


### Refactoring

* fixed import as Score classes have been moved to a different package ([24dc582](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/24dc582a79f34a21a5a86b185e608bbd0960c3e1))

## 1.0.0 (2025-09-12)


### ⚠ BREAKING CHANGES

* created separate package for SpriteManager adjecent classes
* remove width and height parameters from create_projectile in ProjectileFactory, and update all occurrences.
* replaced SpriteManagerImpl with DefaultSpriteManager and adjusted the SpriteManager interface
* added in the constructor of GameControllerImpl agruments to set the difficulty, FPS and the name for the score implementation. Added in the constructor of GameViewImpl an argument to set FPS
* renamed method name of the PlayerAttackHandler getter in Player for consistency sake. Added method is_hurt() in order to understand the type of invulnerability of the Player character (either due to damage or due to a PowerUp)
* added support for CoolDownHandler in PlayerStatusImpl
* added method is_touched to the Player interface
* adjustment to the Area interface's overlap method
* remove direction from projectile
* updated and tested the is_touched() method for Player and updated the Character interface to fit with the new AttackHandler
* updated the shoot method of PlayerImpl to adapt to the new PlayerAttackHandler implementation
* substitution of health variable with health_handler
* changed names of getters and setters in Area and Character, and created a setter for health
* name update to getters and setters of PlayerStatus and Score
* update to the Character interface, as shoot returns a Optional[Projectile]
* removal of reduandant move() method from the Entity interface and fixes to @property method calls
* added PlayerStatus to the Player interface and implementation
* now Rect is used inside the Area class and pygame has been added to the requirements-dev file

### Features

* add HealthRecoveryPowerUp to PowerUpFactory ([0ee854e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0ee854e34e674e42c53e357064eae8609364f004))
* add initial implementation of GeneralAttackHandler and PlayerAttackHandler ([34cdef3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/34cdef36ef06ce18fba4d36bc94318aa906c5b41))
* add interfaces and skeletons for PowerUp, Projectile and their factories. ([f0baf21](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/f0baf21456e24853a5703c47d2d106214fdcee9d))
* add method to remove destroyed items in World ([0bce061](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0bce0615e2a6244792fa914234f1ff308446e9f2))
* add method to remove entity from World ([db4b833](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/db4b833991fdd12a9bd22d11dc3136c71fb54e8e))
* add method to remove entity from World ([882af76](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/882af76a01955d900aa31869b538f246bbc7117c))
* add new enemy formations ([460de29](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/460de296bb695f3da9784b9c87da4d573340d917))
* add ProjectilePowerUp class to track projectiles created during a specific power-up (e.g. Laser) ([981a205](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/981a205df3bf36ce0b2cbf8711d91117b0ceee5d))
* add SpriteManagerProjectile for handling all projectile sprites ([ad6dc8a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ad6dc8a55227df76e13f8515c612aff05cb0fa19))
* add update_power_ups in GameControllerImpl and fix PowerUp classes ([1695ec3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/1695ec3aa84c9737041b011bee2b1fc0cb72fbb0))
* add update_power_ups in GameControllerImpl and fix PowerUp classes ([54399a0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/54399a046fbfe5bd1d12f52b4517c7387f497636))
* add update_power_ups in GameControllerImpl and fix PowerUp classes ([bc2d766](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/bc2d76609df4d8204811f98d4ee205f26d26b8ea))
* add updateProjectile method in GameControllerImpl and fix projectile sprite positions ([12db546](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/12db54618833e451d5bc36043b25c8c5ddc2ad95))
* add updateProjectile method in GameControllerImpl and fix projectile sprite positions ([e98ac83](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e98ac836fb7f5591db8043dab6bef7e0b7f334e6))
* added first menu implementation ([d5d4a07](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d5d4a07118f25e3358505dc44a25831d86454a1a))
* added first version of the Scoreboard implementation (menu and controller integration to follow) ([2f5738f](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2f5738faffec316ba1879c7789ea18cce2f5dbe0))
* added method is_touched to the Player interface ([bd55bb6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/bd55bb62dba940ef5d9cd5f284808b2d1dcc40a4))
* added methods to access the delta property of Entity ([84f1595](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/84f15951ec088988f60df648ff8dc85f3582119d))
* added new methods in PlayerStatus to handle invulnerability ([9c577ea](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9c577ea2347c82c055f97df938d801158557c88a))
* added PlayerStatus to the Player interface and implementation ([447f6cf](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/447f6cfeaf34e8ee7fa156e5f0e3d58fd12fa727))
* added support for ScoreBoard to both GameControllerImpl and MenuImpl ([c78baf2](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/c78baf2d50b846809369dfc9a3d2968580809352))
* completed first implementation of World ([a79e834](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a79e8347ff11b155a361d7c64963f638fa4de400))
* **controller:** add update enemies in game loop ([8704899](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/87048991a303c557056d2ced350a6c927875ca24))
* **controller:** respawn enemy waves to make game endless ([d411df3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d411df3bba63219c7bb99bb62705124a8235fa33))
* creation of PlayerStatus ([9f9933e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9f9933e83e901aa409a77cdaa88f27a8399faf8f))
* creation of the world interface ([2f3e60d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2f3e60d242496901e4329c3f2b8c99a1c445b98a))
* **enemy:** add bat enemy with target tracking ([3d4896f](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/3d4896fa929553d981b295eed1afd4f9f380f488))
* **enemy:** add bird enemy with bouncing movement ([862b74d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/862b74dc6ba8c8ba584ad6dd7f46680864d70de1))
* **enemy:** implement enemy attack system ([84c49bf](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/84c49bfeb8076c4a3813253c834d8cef810b4b63))
* **enemy:** implement enemy formation factory ([4fd2ba6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4fd2ba62d2a9250187bf95abac4d40125b25a4f4))
* first implemenation of Entity, Area, and Position ([5896795](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5896795eea2cda97be4ff7d512ef4a3344548027))
* first implementation of Player, PowerUpHandler and Score ([06b256e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/06b256ee3df4bff5192df5b8829eeff642b39e19))
* first implementation of PowerUp classes ([f7ccade](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/f7ccadee32eef6752f1d0486f07b222e25e48d0c))
* first implementation of World's getters ([7ffcdee](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7ffcdeeecf2513ceedfedb52e7e66c51b545be22))
* **gameplay:** add continuous enemy spawning and advanced combat mechanics ([d654fc5](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d654fc5f95a4d035f199a676939665550ef1fb4d))
* **gameplay:** added further sound effects ([bc326be](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/bc326bebe9dda51919257b29f6962717522975d2))
* implement in-game sound effects ([89c4f5b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/89c4f5b27f06781a4a362a6b285d3b4e990b2343))
* implement ProjectileFatcory ([efadc33](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/efadc33f34890fe3ccc85a65e29508b0b4a75e03))
* implement SoundManager for handling background music ([cb5c290](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/cb5c290f12c373af3300cf1cdae2847f32050da3))
* implementation of Character ([ebc3cf2](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ebc3cf294284da6a1c9dc0380ac315c0a722af0a))
* implementation of HealthRecoveryPowerUp ([55e065d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/55e065d8cc8ffa57ef52195d2c0fabdc77ea780e))
* implementation of PlayerStatus ([fbe0ce9](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/fbe0ce9893070cea7197a6b047c87d231a6e7392))
* implementation of SpriteManagerPowerUp ([7b6f048](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7b6f048b49daa01d8d195935e86e129ea7e0a8d9))
* implementation of the shoot() method ([5a2d6e3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5a2d6e31b28e4375e8b2a5d0d9a0fa074b9e4cfd))
* initial implementation of Projectile and NormalProjectile ([ec5190a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ec5190aded22cec0b39b86b23d656711da219eb9))
* introduction of the CoolDownHandler interface and implementation ([713b8a0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/713b8a0c15755649f3230c3ac652ead1d02a7ddd))
* **menu:** add volume toggle button ([817fcdb](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/817fcdb5b45027453ae8da013823a7f331b91355))
* **Menu:** updated the Menu api. Added support to go through the scoreboard from the score sub-menu ([516add7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/516add72c83868c326c1f1a13f5ecef9d2fbc099))
* **projectiles:** add movement behavior to sound wave projectiles ([b636529](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b636529789a2a68818718d454ba2f50caa391db0))
* update move method in ProjectileImpl for Laser movement and add default projectile sizes in ProjectileFactory ([20ef3ac](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/20ef3ac426ab501c5d3c03d6dfc0346623ce4e60))
* update PowerUp classes and implement specialized types (Laser, Invulnerability, Double Fire) and factory ([a9c5cee](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a9c5cee1cb38185794a3384c8e29e1eb98e184e5))
* update PowerUpHandler to handle timer during pause and track power-up expiration; adjust Laser dimensions and rendering ([732ea6a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/732ea6a6d464168ad47810e96f5be47313459c5a))
* update try_attack in PlayerAttackHandler to handle multiple shots correctly ([86554c8](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/86554c859ffca45ccc6751e3b090f10be1517ce0))
* **view:** add specialized enemy sprite manager ([d71298d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d71298d7597f6471d83e60d4f7296c1946be5dbb))
* **view:** created first version of AbstractSpriteManager ([aeef36d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/aeef36d8036fc671b7ec0f1df53b4d5eff069709))


### Bug Fixes

* added getters and setters for width and height ([4633ed4](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4633ed46bffdae3560df4675e4a6f1dbab1b7715))
* added in the constructor of GameControllerImpl agruments to set the difficulty, FPS and the name for the score implementation. Added in the constructor of GameViewImpl an argument to set FPS ([babece3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/babece3dc0b29dbd5f5a0dd24a960a25062daa0f))
* added support for CoolDownHandler in PlayerStatusImpl ([62834dd](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/62834ddba87ac77b06b1a258ef5278548dee5602))
* added support for fps in Player to properly handle cooldowns ([bfcaa89](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/bfcaa89b35302a66bdb7c8683b20d81673699f0e))
* adjust GameControllerImpl and GeneralAttackHandlerImpl to work with latest dev changes ([a586ac0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a586ac0d59161fdf6205d497603947abc6e1799f))
* adjust GameControllerImpl and GeneralAttackHandlerImpl to work with latest dev changes ([9f0c699](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9f0c699a2feda7adbac43d56f87e09168d6a897a))
* adjusted logic of limit detection for Player movement ([391c102](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/391c10276795b4ff0ff120286a259abc06d9c9b9))
* adjusted to variables' names in try_attack() and creation of PLAYER_PROJECTILE_SPEED ([9e4dabc](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9e4dabc6d9875c71fb4ba3d288214ef89f21ecb7))
* adjustment to the Area interface's overlap method ([35d004e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/35d004e5aa4806d5e39360d7ed4c1e6529c8f4bb))
* attempt to fix compatibility for Python 3.9 in PowerUpHandler and its implementation ([9aa160d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9aa160dd0b99d348dca26361c491bb3caeead28a))
* changed names of getters and setters in Area and Character, and created a setter for health ([085deef](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/085deef9de2c60c5d46c1b4f5d5a8483b0ef5634))
* check if power-up is timed before removing effect in collect_power_up ([7cf839c](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7cf839c33121fad5770a21e4126e0e099f3f4474))
* destroy PowerUp item when collected by player ([5994eda](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5994eda052f715bbbbda194a924bf2d0dc3ebf69))
* name update to getters and setters of PlayerStatus and Score ([b3aff17](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b3aff17b9c20d5ddb20a3a4655d719b62031e7f5))
* now Rect is used inside the Area class and pygame has been added to the requirements-dev file ([e10f904](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e10f9042ed0ba87df28df7dffbae11a8061ed6ef))
* prevent pygame quit and reset display after game ends ([1010a91](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/1010a91da01b623b54332acb83ff336c43c0b5b8))
* **projectiles:** increase movement speed from 0.1 to 1 ([1955c82](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/1955c825ada2b5e7efd90d4e95083a88640bf9dc))
* reduce the probability of shooting projectiles for birds ([c5774ad](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/c5774adbb42c2f35a3604af314883d2e0c6f0adc))
* removal of reduandant move() method from the Entity interface and fixes to [@property](https://github.com/property) method calls ([9ef3d01](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9ef3d016e2bc1d6d6a472c35d747b2527f586ec8))
* remove direction from projectile ([c79dde4](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/c79dde42b9af573b4b43d8d385d9a85765304c6b))
* replaced SpriteManagerImpl with DefaultSpriteManager and adjusted the SpriteManager interface ([e914be0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e914be02f0cb89aea53dd5683d55f1cf9f0f1f17))
* substitution of health variable with health_handler ([2344a23](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2344a23715d529ae5b6d3e35f4f73d4f33c9256b))
* update to the Character interface, as shoot returns a Optional[Projectile] ([cd1d6aa](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/cd1d6aab349954da7493dc268c2ab76d1265afc0))
* update to the World interface to add new methods to add Entities ([3aeeea8](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/3aeeea8418517fbe2df38beedf2d941921cdc852))
* updated and tested the is_touched() method for Player and updated the Character interface to fit with the new AttackHandler ([3cfea6b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/3cfea6bc5e05d45801c9fbf324ec9d0a86c65f5f))
* updated the shoot method of PlayerImpl to adapt to the new PlayerAttackHandler implementation ([7f7436a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7f7436a2a77bbd2f87b1c308e86a427448877a91))


### Documentation

* add documentation for AttackHandler and PowerUpHandler classes ([a9229ee](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a9229ee986cb08e75317d9d1f655b46488a3a0a8))
* add documentation for PowerUp classes ([5c3b45b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5c3b45b584d2ae363f3608fa71086ea9a6fa6c9b))
* added documentation for certain Player adjacent classes ([ec1082e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ec1082ef128a32118646e95de49ba309a3702698))
* added documentation for Character and its implementation ([e76b936](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e76b9363e07e618db097b42c22ef58e60868591e))
* added documentation for the base Model module classes ([f5a6644](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/f5a6644a5d9402361f27cb32f4e3ceb009a7a45a))
* **enemy:** added documentation for enemy_imp ([035d5d6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/035d5d69e3a56200b9e7146e99109a098b3eabe0))
* **enemy:** correct formation docstring in enemy_factory; remove redundant inner imports ([1824bf4](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/1824bf40fa209047c87c1b725f93e96826ec633c))
* first iteration of the documentation for Player ([d0750d3](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d0750d3a5df03e2e99e6251dde2bf3eff8ffedec))


### Tests

* add HealthRecoveryPowerUp creation to PowerUpFactory tests ([11cdfd9](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/11cdfd933ec9d60c8d0fb01f5ca9f44dae8c9a0f))
* add test for DoubleFirePowerUp ([e1a5677](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e1a5677407b78df316b41d27821a70c7a590d252))
* add test for HealthRecoveryPowerUp ([24e2583](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/24e25837b0dc82a9cb89bbcd9cdd00e962b19c44))
* add test for ProjectilePowerUp ([0ea2e42](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0ea2e4266f755a6001d848620fe85d4863146da5))
* add tests for PlayerAttackHandler ([ee94a46](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ee94a46dfaca3fd3371199536418cc85932bc788))
* add tests for PowerUp classes, PowerUpFactory and PowerUpHandler ([07634ea](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/07634ea4979dc3db837da9256754863525817e53))
* add tests for PowerUpImpl ([87880eb](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/87880ebd7079fba06f3a972c54e5af49ff9197f1))
* add tests for Projectile and ProjectileFactory. ([72630a2](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/72630a24dc919531381d7a1545df5b58022e2a49))
* added specific tests for Entity ([ddac412](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ddac412216dfa8ab33aad4ec10c19ba4165eb235))
* added tests for PlayerStatusHandler and Score ([ef79871](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ef79871c83109f740b962adab13bf198a50ef56d))
* created first test for the Player shot ([6d61bc0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/6d61bc0acfd9d421e44a31757ab9819cfc0deb16))
* created test_player class ([ec973e1](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ec973e1d79984cf2ad7777a61f2948274fad8f9b))
* creation of the base movement test for Player ([b049424](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b0494241ffd6a127ca9b8b4c89476c9043ea7474))
* **enemy:** update tests to match new gameplay behavior ([10057aa](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/10057aa3bf0704168f9dc7e0bf8a3d51325c4212))
* fix PowerUp test after property rename ([ddfad3b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ddfad3b7e11607fe4509b87b1593de6dcc5f0464))
* fixed usage of PlayerStatusImpl in test classes ([26b507e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/26b507e540156de1ea5b071bd93b1c537803154a))
* implementation of test to check the behavior of Player movement while going against the edges of the game world ([a3d078d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a3d078d678c0cefcd1d93c1e909ba8d949f932fb))
* remove test_cooldown from test_projectile because cooldown is now handled by CoolDownHandler ([654b08d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/654b08d81e91db4ce21617ca682b2450826f90de))
* remove test_cooldown from test_projectile because cooldown is now handled by CoolDownHandler ([d5b3774](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d5b37740eb36facc4072ac808fd66843d9b14779))
* renaming of the test class for the Player and fixes for methods calls ([4fce6ae](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4fce6ae4e9e08341a2477350f529aaed7b00c9a9))
* update prjectile tests to match new model structure ([9c818be](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9c818be4e50948e6df38fcdea3c5855fdcc8db89))
* update tests for ProjectileFactory ([64feda6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/64feda6e0c6ccc75fa244ea3e264d1656eea3d01))
* update to test_add_points ([a26e070](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a26e0700a2826c050b03a118a2250b091fc666c3))
* update to the shoot test to verify its cooldown ([1c098de](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/1c098de6e5bf414115f04c4233cffb9fbaf173b3))
* updates to movement related tests for Player ([5e32f64](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5e32f64e92a2354dbe4ed4c8ee0eebbe50cb85e6))
* updates to the Player tests due to the introduction of PlayerStatus ([057f65d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/057f65d20ebadd7e8f2ed9b798d5cf216c47cd2a))


### Build and continuous integration

* added permissions to deploy.yml ([fac1445](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/fac144531b6b0ecba4df81cd995f6e02b11ddec0))
* chnaged the assignees ([30fd673](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/30fd6732d74941ab68645cb21b8aeec1c8993732))
* moved permissions inside of jobs ([03c792e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/03c792ee820081651a27736e1106e3603f6faf92))
* moved permissions to check.yml ([82c0219](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/82c0219db7de6d92d36245b8fcc2d3c1b17868f1))
* replaced template with Avian_Blasters ([102e58d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/102e58d1391536567b30b3739658ae0e5b291434))
* set dependecy to pygame_menu to its latest release ([50bf086](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/50bf086c8d3f3b6538641a6f9a34ca14c21c1282))
* updated dry run contains search repository name to artifact ([5f28250](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5f28250d419b9b3415674cf0f7542b0f7f1d6a3b))
* updated names and desciption to fit with the project's current status ([025caca](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/025cacaa428cb0a1e43b4a939bf4b9fad1f922d5))


### General maintenance

* added cli feedback for instances of Game Over ([e563d15](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e563d158cf7120bc895be28fcfc46cd0e36eac9a))
* added import to handle Python 3.9 compatibility in HealthRecoveryPowerUp ([058ecae](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/058ecaef5b48126d780e8d1066482d16b08035aa))
* added imports to handle Python 3.9 compatibility ([b654679](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b654679c9d0a9c6223ddd0950b34d1878490bdab))
* added missing sprites and revamped old ones ([8728944](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/8728944a3ac8f41d31a96ea5e1dc46cea12cc343))
* added scoreboard.txt to .gitgnore ([cff1c8a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/cff1c8a378749d59031def70834565ffb28e65f3))
* adjustment of imports ([d4e13c2](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d4e13c2ec2f70e89e55d2fd8abebb4e299d1edff))
* **controller:** added cli feedback linked to the score being added to the scoreboard or not depending on whether a name has been specified in the menu or not ([b570ede](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b570ede314aa643f660df5e69c4cd15d5bd4037f))
* created separate package for SpriteManager adjecent classes ([dea34ed](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/dea34edfba1fbd1848352db6051adc60761818df))
* fixed imports and base classes definition fro ItemImpl and GeneralAttackHandlerImpl ([fc7a03e](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/fc7a03e9eef5f36378d98be2fa32d3c7b54514c6))
* fixed imports in test_player class ([cf77af1](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/cf77af11a0d2e923697bd836f77f4456928c1441))
* fixed references to Bird enemies in SpriteManager. Added in the command line notes regarding the Pause feature ([15f8320](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/15f832038ddf2e0257abfed451cdbdf8a144c9a6))
* fixed references to Bird enemies in SpriteManager. Added in the command line notes regarding the Pause feature ([281ac64](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/281ac64bd06262b7376110cd5e517bf257a9851b))
* init, creation of interfaces ([a09dc8d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a09dc8d4ed3d1ec347ea00fb78d0e47ad021466c))
* now sprites have transparent backgrounds instead of opaque ones ([a69c425](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a69c42548e501f3e8004bab02d836b69305db9df))
* remove test power-up from game controller ([edec254](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/edec2541194f55f9fd295ff337df0083caf6e46b))
* remove unused imports ([8d16daa](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/8d16daae7320317855a0e92b683990b5b299d5c4))
* removed Direction import in World ([94127b7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/94127b771e8461e33e3ee96b01dfb8300d0db0e2))
* removing imports of Direction ([39c65b6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/39c65b69aad262284107f380de9c77ed93e870b0))
* renamed sprite names and removed unused ones ([4f6c93c](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4f6c93c66a79be1d632b2b5b8133798666b9ef16))
* **ui+controller:** updated score renderer and game over message displayed on cli ([ddc081c](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ddc081c7be4584f26e9c564a3373fd61059c7b74))


### Style improvements

* renamed method name of the PlayerAttackHandler getter in Player for consistency sake. Added method is_hurt() in order to understand the type of invulnerability of the Player character (either due to damage or due to a PowerUp) ([6121aad](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/6121aadcd90300e6b0866dd058ea179e170e58fa))
* update menu and scoreboard theme colors and button styles ([d45732d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d45732d7ae1f2a6401d86e9ed02b9d8df5079497))


### Refactoring

* add Item and ItemImpl classes so that Projectile and PowerUp inherit from Entity through Item ([e355c27](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e355c27e5949a54b90ec67f93d7d4172e4deba92))
* added __cleaner method in WorldImpl to remove void elements ([9463675](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9463675ca7943f463004a302fd9ee0807714cdce))
* added animations for Player and Enemy characters and support for the SpriteManager specific for Player ([ddce223](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ddce22304a0b9e299f13d2bb4d19b26f402ff427))
* added checks for undesired input values in Player related classes ([2b4dbcf](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2b4dbcfda4dd07c1c331e2db8240ea728d8eaad3))
* added further checks for correct inputs in general model classes and those linked to Player ([648fdde](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/648fdde5034a3bdec9b7aedf3772b951e240b51a))
* added pause functionality to the GameController. Moved the revamped sprites in a dedicated sprites folder ([ba534bb](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/ba534bbd61ff8e8f3a1e1b3a5729c728c7c16a64))
* adjusted Player movement so that it correctly handles the interaction with the game boundaries and changes to its movement delta ([2a65466](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2a65466e521805a18d5d5c6ce2dee7513a58211b))
* adjusted scoreboard file closure ([a4b8678](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a4b8678f4b53e180744d364ffa57a71ca4e3ba64))
* adjusted use of constructors for power_up_handler and attack_handler ([2defbea](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2defbea3e7421427739f8bd7b53f678e0031ebbf))
* adjustement to Player movement ([0cd0f80](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0cd0f8072c471d62d82977980e7eb5f72f0ddbac))
* **bat:** updated bat so that it homes in on Player's X axis position when it gets close enough to Player ([6d7b226](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/6d7b2267fbb8907fda9c717ba9eedef69216f2b6))
* **Controller:** added method to updated all related to Player ([12900d7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/12900d7af323a9ebacd818d9bf56f213fc0b139e))
* **controller:** improved FPS handling ([7720514](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7720514c89d4827155d11ec12dc43489a1fde05a))
* **controller:** removed unused imports and added check for correct upload to scoreboard ([608c7d7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/608c7d70b15d7dcdf594316c10806a6ad5134b67))
* **enemy:** fix inheritance structure and remove sprite variants ([4915fd0](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4915fd0aedd24d2e2dde6c161e5af68fdd2cbefc))
* fix Projectile implementation so projectile tests pass ([26b048f](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/26b048f7ad275ce6045cf1d743659275b6a75979))
* implement bird and bat correct formation movement ([4ef3df4](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/4ef3df4e8178d1ce95d315ade486b441b8ab1839))
* integrate CoolDownHandler into AttackHandler classes and update gameloop ([fbac0de](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/fbac0de91fa391c8116b0204b7a986680b72e2eb))
* integrate CoolDownHandler into AttackHandler classes and update gameloop ([6471c23](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/6471c235d9c9115906758bef818c0237319f99f2))
* made separate function to handle the effective movement ([8d15baa](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/8d15baac0e3d9a29670db037cae089710596d74c))
* made sure the Player is defeated if an enemy reaches its same height ([5de7e92](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5de7e920aaee13110b1b3359e5c20053f350ad93))
* **main:** removed controller as it is initialised inside the menu already ([d0937e7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d0937e75a3971b7f40d82c60051b4e5a7a63da79))
* make SpriteManagerPowerUp and SpriteManagerProjectile extend AbstractSpriteManager ([27df91c](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/27df91c26de228f85877b8a5bd0cf820c2ca9963))
* **menu:** adjusted scoreboard to match general arcade game scoreboard behaviour ([a380e73](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a380e7370edad8d47f867c72c78be1dc6b8350f2))
* **MenuImpl:** updated the Scoreboard so it can be reset reactively in the Menu ([c2068de](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/c2068ded8b30f4b23e055d9148f9f41921d899fa))
* **model:** made so apply_effect in InvulnerabilityPowerUp uses the PlayerStatus invulnerability method ([8e524a9](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/8e524a92bbb4c2af71136edac05d1e5e503b7205))
* move enemy formation logic to a separate module named enemy_factory and integrate with GameControllerImpl ([9085555](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/90855553bca984e85848596e772ea03726158d1f))
* move timed powerup management to PowerUpHandler and add type checking to avoid circular import issues ([e555514](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/e555514b0fa78324565020c0b73898ca92a69758))
* **Player:** updated speed of player projectiles, and collision criteria for Player ([06ae984](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/06ae9841f9f3132e7b5b61b06ae3617c87e56ba7))
* readjustment of Player's health-related functions and tests ([b2b940b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/b2b940b8a6d8edb0bf5348b1e5e1c6b0579f7cdf))
* remove circular imports in PowerUp ([5c73bed](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/5c73bed17c68010844a63c4c6409283c7374919d))
* remove duplicated code in GameControllerImpl ([37bee6f](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/37bee6ff9c48c220e1b75bd68a180c62c1dfab0a))
* remove unused imports from multiple classes ([d2455b9](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d2455b91698e9058cf898dd3b594fda266b528e9))
* remove width and height parameters from create_projectile in ProjectileFactory, and update all occurrences. ([9cef386](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/9cef3862c3487c94a48450737594eeeb6143db00))
* removed a magic number in PlayerAttackHandler ([aba3cbb](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/aba3cbb513b177ce7958768de8d73a421c03fd8e))
* removed unused imports ([f117d11](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/f117d11dd857e0da8ecf0882a44e812076cf3004))
* removed unused imports and elements from different classses ([0f81774](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/0f817744ca39a4c9675076122b4b10375646e6c4))
* **sprite_manager_player:** improved sprite selection logic considering power-ups ([2214d8f](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/2214d8ff01f4a134a35d3c8217717abf1eb8925a))
* **SpriteManagerPlayer:** added visual indication for the invulnerability after a hit of Player. Updated Car sprites ([7bc1f83](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/7bc1f83af9884fc29739670666e787056d8722d3))
* started work on scoreboard sub-menu ([080106b](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/080106b17314c8d99bb754cad20a94824fd66aea))
* streamlined cooldown variables ([c3ec276](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/c3ec2763703f88f0aa7ab191e2d9ce045f06f294))
* update enemy to handle to behavior ([a4cd0c6](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/a4cd0c6a1b146762959c0b0bfb39f13edd6e04c1))
* update GameViewImpl to use new SpriteManager design ([bae6b18](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/bae6b186046414ab7b66e4d75689d1631f870da8))
* update to the actual cool-down calculation ([21156ae](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/21156aef05abd315402968882c1842462e628d86))
* updated cooldowns so that they fit in with CoolDownHandler ([137f0e7](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/137f0e7da5a060a6edbbb0119eb203b068f01cdf))
* updated music deactivation logic ([3b1b7d8](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/3b1b7d8ceac648c0b00c45f60026ac649267c229))
* updated the add_points() method so that it also takes into account the score multiplier ([348ad96](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/348ad9686816e6c7793eaa0bfd6de3697de27bbc))
* updated the implementation of PlayerStatusImpl to handle the changes of status in a DRY fashion ([fe4860c](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/fe4860cb13ddf54d3c0ac9e782fa4535990317c4))
* **view:** added support for new Player sprites indicating invincibility and other power-ups being obtained ([d39421a](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/d39421a71e80bb10f1a94303f87394b79132b9eb))
* **view:** removed a magic number and unused imports ([430499d](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/commit/430499d02f14a834b65dc162d360854433cbf5a9))

## [1.0.1](https://github.com/aequitas-aod/template-python-project/compare/1.0.0...1.0.1) (2024-02-02)


### Dependency updates

* **deps:** update dependency pandas to v2.1.2 ([8fe0d36](https://github.com/aequitas-aod/template-python-project/commit/8fe0d36a83c74ff23c059735a69f91ebef4904f3))
* **deps:** update dependency pandas to v2.1.3 ([27eb2b6](https://github.com/aequitas-aod/template-python-project/commit/27eb2b6e5cd7bdac497412095bdd71ee8bc9f12c))
* **deps:** update dependency pandas to v2.1.4 ([cd2b1d4](https://github.com/aequitas-aod/template-python-project/commit/cd2b1d4c3d22d352a89d57794402df9c8779b5c6))
* **deps:** update dependency pandas to v2.2.0 ([b8df6b1](https://github.com/aequitas-aod/template-python-project/commit/b8df6b14bdb94a9e4d290a67ae9090227da61d29))
* **deps:** update dependency scikit-learn to v1.3.2 ([fe7eea2](https://github.com/aequitas-aod/template-python-project/commit/fe7eea22d078a77ed77477a78785c387953888f8))
* **deps:** update dependency scikit-learn to v1.4.0 ([85de0ed](https://github.com/aequitas-aod/template-python-project/commit/85de0ed24d38277ea86a7ac71781631c097e8aaf))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.69 ([fa07343](https://github.com/aequitas-aod/template-python-project/commit/fa07343c199db9cf3a0784abdf1858983f80392c))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.70 ([2f7eb9b](https://github.com/aequitas-aod/template-python-project/commit/2f7eb9b20f5fc44a154c18cdf4ddb413da9819fc))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.71 ([e7efd4f](https://github.com/aequitas-aod/template-python-project/commit/e7efd4f39ac7396621ae9a7182c42975d8756476))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.72 ([17cd38c](https://github.com/aequitas-aod/template-python-project/commit/17cd38c5f6969e7be37be61087c63047d462e00a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.73 ([ceba297](https://github.com/aequitas-aod/template-python-project/commit/ceba297fb66930fa41cfcc36794f37b16d041c60))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.74 ([a7c030d](https://github.com/aequitas-aod/template-python-project/commit/a7c030de41394700cc0cec89358e59a3709377b2))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.75 ([21e6b9a](https://github.com/aequitas-aod/template-python-project/commit/21e6b9af441d069af6c13ccbd55bad63d4a9a841))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.76 ([fcf51ce](https://github.com/aequitas-aod/template-python-project/commit/fcf51ce4d1048739ca4933ef56cefe69b1f25bb9))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.77 ([24c1ad5](https://github.com/aequitas-aod/template-python-project/commit/24c1ad5c7c2a6df6f8519c4bd3bfd9892cac7bdd))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.78 ([4881854](https://github.com/aequitas-aod/template-python-project/commit/488185409ad1263b83838fba5b07136517c9fe52))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.79 ([b09d25f](https://github.com/aequitas-aod/template-python-project/commit/b09d25f30d81f9bc22cee76f3cf2fe72e1589e62))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.80 ([d9e55c5](https://github.com/aequitas-aod/template-python-project/commit/d9e55c51fa21cf880450cbeee619cca167e55cec))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.81 ([d2608f8](https://github.com/aequitas-aod/template-python-project/commit/d2608f87dc1bb2554c4db8bd8fe57fb75512efdb))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.82 ([22b0719](https://github.com/aequitas-aod/template-python-project/commit/22b0719f19296441890e9e6f122df45efd5e095e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.83 ([8f2ec20](https://github.com/aequitas-aod/template-python-project/commit/8f2ec20935428b99b28d412040689e56fa30a07e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.84 ([cb92e70](https://github.com/aequitas-aod/template-python-project/commit/cb92e703568dbf402c51434c510fd97cb6946c52))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.85 ([f05865d](https://github.com/aequitas-aod/template-python-project/commit/f05865d98e638d8c7192bfdb360898b7152400f9))
* **deps:** update node.js to 20.10 ([f393b2a](https://github.com/aequitas-aod/template-python-project/commit/f393b2a2fb2d3aa98b5c5a969ef4df442d5c79de))
* **deps:** update node.js to 20.11 ([63410da](https://github.com/aequitas-aod/template-python-project/commit/63410da68d5122d155caac39b6f99de19d619825))
* **deps:** update node.js to 20.9 ([d107ca2](https://github.com/aequitas-aod/template-python-project/commit/d107ca20dd8414ef39ab6b6b95740b3ae2c75f16))
* **deps:** update node.js to v20 ([61b7e25](https://github.com/aequitas-aod/template-python-project/commit/61b7e250a9afe02465f435c6b709b2fcc872e338))
* **deps:** update python docker tag to v3.12.0 ([b123d48](https://github.com/aequitas-aod/template-python-project/commit/b123d4847e25cc94e86faf1f5ec37a4e0b54e46d))
* **deps:** update python docker tag to v3.12.1 ([ac01a01](https://github.com/aequitas-aod/template-python-project/commit/ac01a014b54008d5c7af4916880413ba864f9a33))


### Bug Fixes

* **release:** include .python-version in MANIFEST.in ([9d794fa](https://github.com/aequitas-aod/template-python-project/commit/9d794faac19b032c5a0f149c3e5e44df018db17b))


### Build and continuous integration

* **deps:** update actions/setup-node action to v4 ([45c9acd](https://github.com/aequitas-aod/template-python-project/commit/45c9acdfed764240e4e150e65a4507205537a16a))
* **deps:** update actions/setup-python action to v5 ([66921e3](https://github.com/aequitas-aod/template-python-project/commit/66921e3580f3223689adf1665a323befbd9b3272))

## 1.0.0 (2023-10-12)


### Features

* add renaming script ([ed33dbc](https://github.com/aequitas-aod/template-python-project/commit/ed33dbc03a68a605e6df7a9465c6985ec9d1e130))
* first commit ([6ddc082](https://github.com/aequitas-aod/template-python-project/commit/6ddc08296facfe64fe912fcd00a255adb2806193))


### Dependency updates

* **deps:** node 18.18 ([73eec49](https://github.com/aequitas-aod/template-python-project/commit/73eec49c6fc53fe3158a0b94be99dcaf6eb328eb))
* **deps:** update dependencies ([0be2f8d](https://github.com/aequitas-aod/template-python-project/commit/0be2f8deb9b8218e509ea0926ceeb78a7a2baa70))
* **deps:** update python docker tag to v3.11.6 ([199ffe6](https://github.com/aequitas-aod/template-python-project/commit/199ffe6a498c6b26d358d97ac2ef7046da68e268))


### Bug Fixes

* readme ([f12fb0b](https://github.com/aequitas-aod/template-python-project/commit/f12fb0b17c08a18a7e145199234dc38d43fd0ddb))
* release workflow ([9c84ec1](https://github.com/aequitas-aod/template-python-project/commit/9c84ec1497a1f8c6c438a248107746df0fa7c612))
* renovate configuration ([0db8978](https://github.com/aequitas-aod/template-python-project/commit/0db89788ad8bef935fa97b77e7fa05aca749da28))


### Build and continuous integration

* enable semantic release ([648759b](https://github.com/aequitas-aod/template-python-project/commit/648759ba41fda0cad343493709a57bcb908f7229))
* fix release by installing correct version of node ([d809f17](https://github.com/aequitas-aod/template-python-project/commit/d809f17fc96c7295e0ec526161a56f558d49aa47))


### General maintenance

* **ci:** dry run release on testpypi for template project ([b90a25a](https://github.com/aequitas-aod/template-python-project/commit/b90a25a0f1f439e0bf548eec0bfae21b1f8c44b1))
* **ci:** use jq to parse package.json ([66af494](https://github.com/aequitas-aod/template-python-project/commit/66af494bc406d4b9b649153f910016cceb1b63ce))
* initial todo-list ([154e024](https://github.com/aequitas-aod/template-python-project/commit/154e024ac1bb8a1f1c99826ab2ed6a28e703a513))
* remove useless Dockerfile ([0272af7](https://github.com/aequitas-aod/template-python-project/commit/0272af71647e254f7622d38ace6000f0cbc7f17d))
* write some instructions ([7da9554](https://github.com/aequitas-aod/template-python-project/commit/7da9554a6e458c5fc253a222b295fbeb6a7862ec))
