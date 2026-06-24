// ═══════════════════════════════════════════════════════════
// 🔬  ArisEdu Lab Guide Assistant (LabXChange Style)
// ═══════════════════════════════════════════════════════════
(function () {
    'use strict';

    // Only activate on pages inside the /labs/ directory
    if (!window.location.pathname.includes('/labs/')) return;

    // --- Guide Database (Pre-populated for key labs) ---
    const DECORATED_GUIDES = {
      "chemistry_lab.html": {
        category: "Chemistry",
        title: "Chemical Reactions",
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">The Chemistry of Reactions</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            Chemical reactions happen when atomic bonds are broken and formed. Atoms rearrange themselves to produce entirely new substances with distinct physical and chemical traits.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: #34d399; margin-bottom: 0.25rem;">🔑 Key Concepts</h4>
            <ul style="list-style-type: disc; padding-left: 1.25rem; font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; space-y: 0.25rem;">
              <li><strong>Reactants:</strong> The initial substances you combine.</li>
              <li><strong>Products:</strong> The newly formed resulting chemicals.</li>
              <li><strong>Observations:</strong> Gas generation, color shifts, and precipitation prove a chemical change occurred.</li>
            </ul>
          </div>
        `,
        materials: [
          "HCl (Hydrochloric Acid) - Strong acid",
          "NaOH (Sodium Hydroxide) - Strong base",
          "NaHCO3 (Baking Soda) - Carbonate powder",
          "CH3COOH (Vinegar) - Weak acid",
          "AgNO3 (Silver Nitrate) - Solution salt",
          "NaCl (Table Salt) - Halide salt",
          "CuSO4 (Copper Sulfate) - Transition metal salt",
          "Fe (Iron Nail) - Pure metal structure",
          "Phenolphthalein - pH indicator"
        ],
        protocol: [
          "Select 'HCl (Hydrochloric Acid)' on the reagent shelf and click 'Add to Beaker'.",
          "Next, select 'Phenolphthalein' (pH indicator) and add it. Notice it stays colorless in acid.",
          "Select 'NaOH (Sodium Hydroxide)' on the shelf and click 'Add to Beaker'. Watch the pH level change and the solution turn bright pink!",
          "Click 'Reset' to clear the beaker.",
          "Select 'CuSO4 (Copper Sulfate)' and insert it, then add 'Fe' (Iron Nail). Observe the copper placing itself on the iron as a brown displacement deposit."
        ],
        assessment: {
          question: "What is the primary indicator of a chemical reaction when baking soda (carbonates) interacts with hydrochloric acid?",
          options: [
            "No visual change occurs whatsoever",
            "Vigorous fizzing and bubble formation (release of CO2 gas)",
            "The beaker turns into a solid block of metallic copper"
          ],
          correctIndex: 1,
          explanation: "Acids react with carbonates or bicarbonates to produce carbon dioxide gas (CO₂), which presents as strong effervescence (bubbling/fizzing)."
        }
      },
      "physics_sandbox.html": {
        category: "Physics",
        title: "Projectile, Pendulum & Collisions",
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">Kinematics & Gravity</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            A projectile is any object launched into space upon which the only acting force is gravity. Under constant gravity, its horizontal speed remains steady while its vertical velocity changes, creating a parabolic arc.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: #60a5fa; margin-bottom: 0.25rem;">🔑 Key Aspects</h4>
            <div style="font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; line-height: 1.4;">
              <p>• Horizontal Range: Peak range is achieved at exactly 45 degrees without air resistance.</p>
              <p>• Peak Height: Height increases with larger, steeper launch angles.</p>
            </div>
          </div>
        `,
        materials: [
          "Projectile Launcher with adjustable barrel angle",
          "Launch trigger mechanism",
          "Velocity speed controls",
          "Reference ground grid and landing target"
        ],
        protocol: [
          "Set the launch angle to 45 degrees.",
          "Set the launch speed to 50 m/s and click 'Launch'. Notice the landing range.",
          "Change the angle to 60 degrees. Fire again and observe if it goes higher but lands closer.",
          "Now switch the angle to 30 degrees. Fire and compare its range with the 60-degree trial (Complementary mechanics!).",
          "Switch to the 'Pendulum' or 'Collisions' tab at the top to experiment with alternative motion mechanics."
        ],
        assessment: {
          question: "Which angle results in the maximum horizontal displacement (range) for a projectile on flat ground?",
          options: [
            "15° launch angle",
            "45° launch angle",
            "75° launch angle"
          ],
          correctIndex: 1,
          explanation: "A launch angle of 45 degrees perfectly balances horizontal velocity propagation with vertical flight time, yielding maximum horizontal displacement."
        }
      },
      "biology_lab.html": {
        category: "Biology",
        title: "Cell Explorer Microscope",
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">Cellular Architectures</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            Cells are categorized into Eukaryotes (complex cells with a nucleus like animal & plant units) and Prokaryotes (simple single-cell units without a nucleus like bacteria). Microscope observation lets us identify their component organelles.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: #34d399; margin-bottom: 0.25rem;">🔑 Key Structures</h4>
            <ul style="list-style-type: disc; padding-left: 1.25rem; font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; space-y: 0.25rem;">
              <li><strong>Cell Wall:</strong> Provides boundary safety for plants & bacteria (absent in animals).</li>
              <li><strong>Nucleus:</strong> Contains DNA, acts as the cell control center.</li>
              <li><strong>Chloroplasts:</strong> Power factories in plant cells that run photosynthesis.</li>
            </ul>
          </div>
        `,
        materials: [
          "Virtual Microscope focal lens controls",
          "Animal cell sample slide",
          "Plant cell sample slide",
          "Bacterial cell sample slide"
        ],
        protocol: [
          "Load the Animal Cell slide and focus the camera. Point out the nucleus and outer cell membrane.",
          "Switch slides and load the Plant Cell slide. Adjust focus.",
          "Look for the thick rigid Cell Wall framing the plant cell and the small green Chloroplast dots inside.",
          "Load the Bacteria slide, focus, and observe the thin hair-like flagellum and lack of a central nucleus.",
          "Discuss how organelle diversity accommodates separate ecological lifestyles."
        ],
        assessment: {
          question: "Which slide sample exhibits green chloroplast organelles that capture sunlight?",
          options: [
            "Plant Cell slide",
            "Animal Cell slide",
            "Bacteria slide"
          ],
          correctIndex: 0,
          explanation: "Plant cells utilize green chlorophyll-filled Chloroplast organelles to conduct photosynthesis, extracting chemical energy from solar radiation."
        }
      },
      "earth_science_lab.html": {
        category: "Earth Science",
        title: "Interactive Earth Models",
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">Crust Boundaries & Activity</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            Earth's rigid outer shell is cracked into puzzle pieces called tectonic plates. Floated along convective current pathways in the mantle, plates diverge, converge, or scrape against one another to shape planet topography.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: #3b82f6; margin-bottom: 0.25rem;">🔑 Crust Margins</h4>
            <ul style="list-style-type: disc; padding-left: 1.25rem; font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; space-y: 0.25rem;">
              <li><strong>Convergent:</strong> Plates crash (forms mountain ranges & volcanoes).</li>
              <li><strong>Divergent:</strong> Plates split (forms mid-ocean crust ridges).</li>
              <li><strong>Transform:</strong> Plates grind (creates strike-slip fault lines).</li>
            </ul>
          </div>
        `,
        materials: [
          "Tectonic motion driver controls",
          "Oceanic crust layers",
          "Continental crust plates",
          "Mantle convection speed simulation"
        ],
        protocol: [
          "Slide plate arrows apart to establish a Divergent Boundary. Watch how molten magma wells up to fill the rift.",
          "Configure a Convergent interface where Continental meets Oceanic crust.",
          "Notice how the dense oceanic plate subducts underneath the lighter continental plate, creating volcanoes.",
          "Initialize plate slip paths (Transform Boundary) to witness sliding friction stress.",
          "Notice the earthquake focal points that emerge near fault fractures."
        ],
        assessment: {
          question: "Which boundary margin is directly responsible for pulling crust apart and building mid-ocean rifts?",
          options: [
            "Transform Boundary",
            "Convergent Boundary",
            "Divergent Boundary"
          ],
          correctIndex: 2,
          explanation: "Divergent boundaries pull plates apart, allowing magma to overflow and create fresh seafloor along spreading rifts."
        }
      },
      "unit_circle.html": {
        category: "Mathematics",
        title: "The Unit Circle",
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">Trig Functions Visualized</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            The unit circle is centered at (0,0) with a radius of 1. The coordinates of any point on the circle at angle theta are exactly (cos theta, sin theta). This links geometry perfectly with algebraic sine and cosine properties.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: #c084fc; margin-bottom: 0.25rem;">🔑 Functions</h4>
            <div style="font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; line-height: 1.4;">
              <p>• Cosine (x-axis projection): cos(θ)</p>
              <p>• Sine (y-axis projection): sin(θ)</p>
              <p>• Tangent (slope coefficient): sin(θ) / cos(θ)</p>
            </div>
          </div>
        `,
        materials: [
          "Coordinate grid overlay with unit radius",
          "Rotatable angle arm",
          "Sine and Cosine length projectors",
          "Quadrant sign indicators (+ / -)"
        ],
        protocol: [
          "Sweep the coordinate arm to 0 radians (0 degrees). Observe coordinate positions (1, 0).",
          "Drag the angle arm to 30 degrees and check the sine and cosine lengths.",
          "Move the angle arm to exactly 90 degrees. Note how cosine goes to 0 and sine reaches peak 1.",
          "Drag into Quadrant 2 (e.g., 135 degrees). Notice how the x-value (cosine) flips to negative, while y (sine) remains positive.",
          "Sweep through Quadrant 3 and observe both sine and cosine showing negative values."
        ],
        assessment: {
          question: "At an angle of 180 degrees (straight-left on grid), what are the sine and cosine values, respectively?",
          options: [
            "cos = 0, sin = 1",
            "cos = -1, sin = 0",
            "cos = 1, sin = -1"
          ],
          correctIndex: 1,
          explanation: "At 180 degrees, the point rests on the far-left coordinate axis: x = cos(180°) = -1 and y = sin(180°) = 0."
        }
      }
    };

    function deriveSubjectCategory(filename) {
      if (/chem|reaction|phase|gas|titration|electro|calor|equilibrium|stoich|solut|periodic|molecular|nuclear|acid/i.test(filename)) {
        return { category: "Chemistry", color: "#f59e0b" };
      }
      if (/physic|project|pendulum|collis|wave|circuit|optic|incline|field|spring|thermo|doppler|magnet|fluid|centripetal|standing/i.test(filename)) {
        return { category: "Physics", color: "#f59e0b" };
      }
      if (/biol|cell|photo|enzyme|dna|select|nerv|mito|ecosys|respir|genet|protein|immune|meio|circulat|plant|digest|evolut/i.test(filename)) {
        return { category: "Biology", color: "#22c55e" };
      }
      if (/marine|coral|current|tide|depth|vent|coastal|biolum|spill|acidific|kelp|plankt|tsunami|estuary|whale/i.test(filename)) {
        return { category: "Marine Science", color: "#22c55e" };
      }
      if (/solar|moon|astro|galaxies|exoplanet|spectro|gravity|season|cosmic|stellar|black|binary|rocket|nebula/i.test(filename)) {
        return { category: "Astronomy", color: "#3b82f6" };
      }
      if (/plate|rock|water|volcano|weather|earthq|glacier|atmos|carbon|soil|mineral|climate|ground|fossil|erosion/i.test(filename)) {
        return { category: "Earth Science", color: "#3b82f6" };
      }
      return { category: "Mathematics", color: "#a855f7" };
    }

    function buildStandardGuide(filename) {
      const cleanName = filename.replace(/\.(html|js|php)$/i, '').replace(/_/g, ' ');
      const title = cleanName.charAt(0).toUpperCase() + cleanName.slice(1);
      const subInfo = deriveSubjectCategory(filename);

      return {
        category: subInfo.category,
        title: title,
        theory: `
          <h3 style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem;">Core Scientific Principle</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 1rem;">
            Welcome to the <strong>${title}</strong> interactive workspace. This module belongs to the study of <strong>${subInfo.category}</strong>.
          </p>
          <div style="padding: 0.85rem; background: #1e293b; border-radius: 0.5rem; border: 1px solid #334155;">
            <h4 style="font-size: 0.8rem; font-weight: 700; color: ${subInfo.color}; margin-bottom: 0.25rem;">🔥 Educational Goals</h4>
            <ul style="list-style-type: disc; padding-left: 1.25rem; font-size: 0.75rem; color: #cbd5e1; margin-top: 0.25rem; space-y: 0.25rem;">
              <li>Observe physical, mathematical, or organic limits and behaviors.</li>
              <li>Develop scientific intuition through visual triggers.</li>
              <li>Identify correlations between custom input variables and reactions.</li>
            </ul>
          </div>
        `,
        materials: [
          `Interactive ${title} simulator interface`,
          "Real-time visual monitoring dashboard",
          "Parameter manipulation slider panel",
          "Reset, pause, and starting toggles"
        ],
        protocol: [
          `Open the ${title} simulation dashboard on the main screen area.`,
          "Inspect the initial state and familiarize yourself with default constants.",
          "Alter variables slowly and observe how each change translates to reaction spikes, waves, or cycles.",
          "Document your observed values and experimental hypothesis in the 'Notebook' section.",
          "Click the reset buttons to clear visual layouts and initiate fresh trials."
        ],
        assessment: {
          question: `What primary training benefit does the interactive ${title} virtual sandbox deliver?`,
          options: [
            "It maps algebraic and scientific constants onto visual reactions to cultivate concrete intuition",
            "It acts as a static document overlay with zero interactive responsive triggers",
            "It runs pre-recorded video files that cannot be edited or reset"
          ],
          correctIndex: 0,
          explanation: "Modern interactive simulation environments respond dynamically to student input, demonstrating the exact physical equations that drive the system."
        }
      };
    }

    const path = window.location.pathname;
    const filename = path.split('/').pop() || "";
    let guide = DECORATED_GUIDES[filename] || buildStandardGuide(filename);

    const WORKSPACE_SECTIONS = ['overview', 'materials', 'protocol', 'assessment', 'notebook'];
    let currentSectionIndex = 0;
    let notesSaveTimeout = null;

    // --- CSS Injection ---
    const helperStyle = document.createElement('style');
    helperStyle.id = 'aris-lab-helper-styles';
    helperStyle.innerHTML = `
      body {
        transition: padding-left 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      }
      .lab-sidebar-btn {
        position: fixed;
        left: 20px;
        top: 80px;
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
        color: #ffffff;
        font-weight: 600;
        font-size: 0.75rem;
        padding: 0.5rem 0.9rem;
        border-radius: 9999px;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        cursor: pointer;
        border: none;
        transition: all 0.2s ease;
        outline: none;
        font-family: 'Poppins', sans-serif;
      }
      .lab-sidebar-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
      }
      .lab-sidebar {
        position: fixed;
        left: -400px;
        top: 50px;
        bottom: 0;
        width: 400px;
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
        z-index: 10000;
        display: flex;
        flex-direction: column;
        color: #f1f5f9;
        font-family: 'Poppins', sans-serif;
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.5);
        transition: left 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .lab-sidebar.open {
        left: 0;
      }
      .lab-sidebar-header {
        padding: 1.25rem;
        border-bottom: 1px solid #1e293b;
        background-color: #020617;
        position: relative;
      }
      .lab-sidebar-close {
        position: absolute;
        right: 1rem;
        top: 1.25rem;
        background: transparent;
        border: none;
        color: #94a3b8;
        font-size: 1.1rem;
        cursor: pointer;
        padding: 0;
      }
      .lab-sidebar-close:hover {
        color: #ffffff;
      }
      .lab-sidebar-tabs {
        display: flex;
        border-bottom: 1px solid #1e293b;
        background-color: #020617;
        font-size: 10px;
        font-weight: 700;
        overflow-x: auto;
      }
      .lab-sidebar-tab-btn {
        flex: 1;
        padding: 0.75rem 0.5rem;
        text-align: center;
        background: transparent;
        border: none;
        border-bottom: 2px solid transparent;
        color: #94a3b8;
        cursor: pointer;
        font-weight: bold;
        transition: all 0.2s;
        text-transform: uppercase;
        font-size: 10px;
        white-space: nowrap;
      }
      .lab-sidebar-tab-btn:hover {
        color: #ffffff;
      }
      .lab-sidebar-tab-btn.active {
        color: #10b981;
        border-bottom-color: #10b981;
      }
      .lab-sidebar-content {
        flex: 1;
        padding: 1.25rem;
        overflow-y: auto;
      }
      .lab-sidebar-footer {
        padding: 0.75rem 1.25rem;
        border-top: 1px solid #1e293b;
        background-color: #020617;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .lab-sidebar-footer button {
        padding: 0.4rem 0.8rem;
        background-color: #1e293b;
        color: #cbd5e1;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: background 0.2s;
      }
      .lab-sidebar-footer button:hover {
        background-color: #334155;
      }
      .lab-sidebar-footer button:disabled {
        opacity: 0.3;
        cursor: not-allowed;
      }
      .lab-sidebar-footer button.primary {
        background-color: #10b981;
        color: #ffffff;
      }
      .lab-sidebar-footer button.primary:hover {
        background-color: #059669;
      }
      .lab-sidebar-checkbox-row {
        display: flex;
        align-items: start;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
        font-size: 0.8rem;
        color: #cbd5e1;
        cursor: pointer;
      }
      .lab-sidebar-checkbox-row input {
        margin-top: 0.15rem;
        cursor: pointer;
      }
      .lab-sidebar-checkbox-row input:checked + label {
        text-decoration: line-through;
        opacity: 0.5;
      }
      .opt-button {
        width: 100%;
        text-align: left;
        padding: 0.6rem 0.75rem;
        border-radius: 0.375rem;
        border: 1px solid #1e293b;
        background-color: rgba(2, 6, 23, 0.4);
        color: #cbd5e1;
        font-size: 0.75rem;
        cursor: pointer;
        transition: all 0.2s;
        display: flex;
        align-items: start;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
      }
      .opt-button:hover {
        background-color: rgba(30, 41, 59, 0.6);
        color: #ffffff;
      }
      .opt-index {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 1.25rem;
        height: 1.25rem;
        background-color: #1e293b;
        border-radius: 9999px;
        font-size: 9px;
        font-weight: bold;
        flex-shrink: 0;
        color: #94a3b8;
      }
    `;
    document.head.appendChild(helperStyle);

    // --- HTML Construction ---
    const sidebarHtml = `
      <div id="aris-lab-sidebar" class="lab-sidebar">
        <div class="lab-sidebar-header">
          <span style="font-size: 9px; font-weight: bold; color: #10b981; text-transform: uppercase; letter-spacing: 0.05em;" id="sb-category">${guide.category} Guide</span>
          <h2 style="font-size: 0.95rem; font-weight: bold; color: #ffffff; margin-top: 2px;" id="sb-title">${guide.title}</h2>
          <button onclick="window._toggleLabSidebar()" class="lab-sidebar-close">✕</button>
        </div>
        <div class="lab-sidebar-tabs">
          <button onclick="window._setSidebarTab('overview')" id="sb-tab-overview" class="lab-sidebar-tab-btn active">Theory</button>
          <button onclick="window._setSidebarTab('materials')" id="sb-tab-materials" class="lab-sidebar-tab-btn">Materials</button>
          <button onclick="window._setSidebarTab('protocol')" id="sb-tab-protocol" class="lab-sidebar-tab-btn">Protocol</button>
          <button onclick="window._setSidebarTab('assessment')" id="sb-tab-assessment" class="lab-sidebar-tab-btn">Quiz</button>
          <button onclick="window._setSidebarTab('notebook')" id="sb-tab-notebook" class="lab-sidebar-tab-btn">Notebook</button>
        </div>
        <div class="lab-sidebar-content" id="sb-dynamic-content">
          <!-- Guided sections -->
        </div>
        <div class="lab-sidebar-footer">
          <button id="sb-btn-prev" onclick="window._navigateSidebar(-1)">Prev</button>
          <span style="font-size: 0.7rem; color: #64748b;" id="sb-progression">1 / 5</span>
          <button id="sb-btn-next" onclick="window._navigateSidebar(1)" class="primary">Next</button>
        </div>
      </div>
      <button id="aris-lab-sidebar-toggle-btn" class="lab-sidebar-btn" onclick="window._toggleLabSidebar()">
        <svg style="width: 14px; height: 14px; fill: none; stroke: currentColor; stroke-width: 2;" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
        <span>Lab Guide</span>
      </button>
    `;

    const elWrap = document.createElement('div');
    elWrap.innerHTML = sidebarHtml;
    
    // Safely append to helper or body immediately or on DOM load
    function initSidebar() {
      if (document.getElementById("aris-lab-sidebar")) return; // prevent double inject
      document.body.appendChild(elWrap);
      window._renderSidebarActiveSection();
    }

    if (document.readyState !== "loading") {
      initSidebar();
    } else {
      document.addEventListener("DOMContentLoaded", initSidebar);
    }

    // --- State Toggles ---
    let sidebarOpen = false;

    window._toggleLabSidebar = function() {
      sidebarOpen = !sidebarOpen;
      const sbEl = document.getElementById("aris-lab-sidebar");
      const btnEl = document.getElementById("aris-lab-sidebar-toggle-btn");
      
      if (sbEl) {
        if (sidebarOpen) {
          sbEl.classList.add("open");
          if (window.innerWidth >= 768) {
            document.body.style.paddingLeft = "400px";
          }
          if (btnEl) btnEl.style.left = "420px";
        } else {
          sbEl.classList.remove("open");
          document.body.style.paddingLeft = "0px";
          if (btnEl) btnEl.style.left = "20px";
        }
      }
    };

    window._setSidebarTab = function(sectionKey) {
      currentSectionIndex = WORKSPACE_SECTIONS.indexOf(sectionKey);
      window._renderSidebarActiveSection();
    };

    window._navigateSidebar = function(direction) {
      const newIdx = currentSectionIndex + direction;
      if (newIdx >= 0 && newIdx < WORKSPACE_SECTIONS.length) {
        currentSectionIndex = newIdx;
        window._renderSidebarActiveSection();
      }
    };

    window._submitSidebarClickQuiz = function(index) {
      const feedbackEl = document.getElementById("sb-quiz-feedback");
      if (!feedbackEl) return;

      feedbackEl.style.display = "block";
      feedbackEl.style.padding = "0.75rem";
      feedbackEl.style.borderRadius = "0.375rem";
      feedbackEl.style.fontSize = "0.75rem";
      feedbackEl.style.marginTop = "0.75rem";
      feedbackEl.style.lineHeight = "1.4";

      if (index === guide.assessment.correctIndex) {
        feedbackEl.style.backgroundColor = "rgba(6, 78, 59, 0.7)";
        feedbackEl.style.border = "1px solid #065f46";
        feedbackEl.style.color = "#a7f3d0";
        feedbackEl.innerHTML = `
          <div style="font-weight: bold; margin-bottom: 0.25rem;">✓ Correct! Excellent analysis.</div>
          <div>${guide.assessment.explanation}</div>
        `;
      } else {
        feedbackEl.style.backgroundColor = "rgba(153, 27, 27, 0.7)";
        feedbackEl.style.border = "1px solid #991b1b";
        feedbackEl.style.color = "#fca5a5";
        feedbackEl.innerHTML = `
          <div style="font-weight: bold; margin-bottom: 0.25rem;">✗ Keep learning! Try again.</div>
          <div>Reflect on the scientific theory in the first tab and select another possibility.</div>
        `;
      }
    };

    window._saveSidebarJournalNotes = function(val) {
      const statusEl = document.getElementById("sb-journal-status");
      if (statusEl) {
        statusEl.textContent = "Writing...";
        statusEl.style.color = "#10b981";
      }
      localStorage.setItem(`lab_notes_${filename}`, val);

      if (notesSaveTimeout) clearTimeout(notesSaveTimeout);
      notesSaveTimeout = setTimeout(() => {
        if (statusEl) {
          statusEl.textContent = "Saved locally";
          statusEl.style.color = "#64748b";
        }
      }, 700);
    };

    window._clearSidebarJournalNotes = function() {
      if (confirm("Are you sure you want to clear your lab journal entries for this module?")) {
        const textarea = document.getElementById("sb-notes-textarea");
        if (textarea) textarea.value = "";
        localStorage.removeItem(`lab_notes_${filename}`);
        const statusEl = document.getElementById("sb-journal-status");
        if (statusEl) statusEl.textContent = "Cleared";
      }
    };

    window._renderSidebarActiveSection = function() {
      const activeSec = WORKSPACE_SECTIONS[currentSectionIndex];

      WORKSPACE_SECTIONS.forEach(sec => {
        const btn = document.getElementById(`sb-tab-${sec}`);
        if (btn) {
          if (sec === activeSec) {
            btn.classList.add("active");
          } else {
            btn.classList.remove("active");
          }
        }
      });

      const contentBox = document.getElementById("sb-dynamic-content");
      if (!contentBox) return;

      if (activeSec === 'overview') {
        contentBox.innerHTML = guide.theory;
      } else if (activeSec === 'materials') {
        let listHtml = `<h3 style="font-size: 0.9rem; font-weight: bold; color: #ffffff; margin-bottom: 0.75rem;">🔬 Essential Materials</h3>`;
        guide.materials.forEach((item, index) => {
          listHtml += `
            <div class="lab-sidebar-checkbox-row">
              <input type="checkbox" id="sb-mat-${index}" />
              <label for="sb-mat-${index}">${item}</label>
            </div>
          `;
        });
        contentBox.innerHTML = listHtml;
      } else if (activeSec === 'protocol') {
        let listHtml = `<h3 style="font-size: 0.9rem; font-weight: bold; color: #ffffff; margin-bottom: 0.75rem;">🧪 Experimental Protocol</h3>`;
        guide.protocol.forEach((step, index) => {
          listHtml += `
            <div style="padding: 0.75rem; background: rgba(30, 41, 59, 0.4); border: 1px solid #1e293b; border-radius: 0.5rem; margin-bottom: 0.5rem; display: flex; align-items: start; gap: 0.5rem;">
              <input type="checkbox" id="sb-step-${index}" style="margin-top: 0.15rem; cursor: pointer;" />
              <div style="flex-1; font-size: 0.8rem; color: #cbd5e1; line-height: 1.4;">
                <label for="sb-step-${index}" style="cursor: pointer;">
                  <strong style="color: #10b981;">Step ${index + 1}:</strong> ${step}
                </label>
              </div>
            </div>
          `;
        });
        contentBox.innerHTML = listHtml;
      } else if (activeSec === 'assessment') {
        let assessmentHtml = `
          <h3 style="font-size: 0.9rem; font-weight: bold; color: #ffffff; margin-bottom: 0.5rem;">🧠 Understanding Check</h3>
          <p style="font-size: 0.8rem; color: #cbd5e1; margin-bottom: 0.75rem; line-height: 1.4; font-weight: 600;">${guide.assessment.question}</p>
          <div>
        `;
        guide.assessment.options.forEach((opt, index) => {
          assessmentHtml += `
            <button onclick="window._submitSidebarClickQuiz(${index})" class="opt-button">
              <span class="opt-index">${String.fromCharCode(65 + index)}</span>
              <span style="flex:1;">${opt}</span>
            </button>
          `;
        });
        assessmentHtml += `
          </div>
          <div id="sb-quiz-feedback" style="display:none;"></div>
        `;
        contentBox.innerHTML = assessmentHtml;
      } else if (activeSec === 'notebook') {
        const stored = localStorage.getItem(`lab_notes_${filename}`) || "";
        let notesHtml = `
          <h3 style="font-size: 0.9rem; font-weight: bold; color: #ffffff; margin-bottom: 0.25rem;">✍️ Digital Lab Journal</h3>
          <p style="font-size: 0.7rem; color: #94a3b8; margin-bottom: 0.5rem; line-height: 1.3;">
            Draft observations or trial variables here. Your entries save automatically.
          </p>
          <textarea id="sb-notes-textarea" oninput="window._saveSidebarJournalNotes(this.value)" placeholder="Write your notes here..." style="width: 100%; height: 260px; padding: 0.5rem; font-size: 0.75rem; color: #e2e8f0; background-color: #020617; border-size: 1px; border-color: #1e293b; border-style: solid; border-radius: 0.375rem; font-family: monospace; resize: none; outline: none; line-height: 1.4;">${stored}</textarea>
          <div style="display: flex; align-items: center; justify-content: space-between; font-size: 0.7rem; color: #64748b; margin-top: 0.25rem;">
            <span id="sb-journal-status">Saved locally</span>
            <span onclick="window._clearSidebarJournalNotes()" style="color: #f87171; cursor: pointer;">Clear Journal</span>
          </div>
        `;
        contentBox.innerHTML = notesHtml;
      }

      // Sync navigation controls
      const prog = document.getElementById("sb-progression");
      if (prog) prog.textContent = `${currentSectionIndex + 1} / ${WORKSPACE_SECTIONS.length}`;

      const prev = document.getElementById("sb-btn-prev");
      if (prev) prev.disabled = currentSectionIndex === 0;

      const next = document.getElementById("sb-btn-next");
      if (next) {
        if (currentSectionIndex === WORKSPACE_SECTIONS.length - 1) {
          next.textContent = "Close";
          next.onclick = function() { window._toggleLabSidebar(); };
        } else {
          next.textContent = "Next";
          next.onclick = function() { window._navigateSidebar(1); };
        }
      }
    };
})();
