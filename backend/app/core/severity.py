import numpy as np
from typing import Dict, Any, List

class SeverityEngine:
    """
    Quantifies defect severity based on spatial area, morphological properties,
    peak anomaly intensity, and critical engineering zones.
    """
    def __init__(self, critical_mask: np.ndarray = None):
        self.critical_mask = critical_mask

    def calculate_severity(self, heatmap: np.ndarray, threshold: float = 0.5) -> Dict[str, Any]:
        """
        Calculates actionable severity metrics from the anomaly heatmap.
        """
        binary_mask = (heatmap >= threshold).astype(np.uint8)
        area_pixels = int(np.sum(binary_mask))
        total_pixels = heatmap.shape[0] * heatmap.shape[1]
        area_pct = (area_pixels / total_pixels) * 100.0
        peak_intensity = float(np.max(heatmap)) if heatmap.size > 0 else 0.0

        # Weighted severity index (0 - 100)
        severity_index = min(100.0, (area_pct * 10.0) + (peak_intensity * 40.0))

        if severity_index < 25.0:
            grade = "MINOR"
        elif severity_index < 60.0:
            grade = "MODERATE"
        elif severity_index < 85.0:
            grade = "MAJOR"
        else:
            grade = "CRITICAL"

        return {
            "grade": grade,
            "severity_index": round(severity_index, 2),
            "affected_area_pct": round(area_pct, 2),
            "peak_intensity": round(peak_intensity, 4),
            "action_recommendation": self._get_action(grade)
        }

    def _get_action(self, grade: str) -> str:
        actions = {
            "MINOR": "Pass with Log",
            "MODERATE": "Rework Station",
            "MAJOR": "Quarantine / Manual Inspection",
            "CRITICAL": "Immediate Line Halt & Scrap"
        }
        return actions.get(grade, "Inspect")
