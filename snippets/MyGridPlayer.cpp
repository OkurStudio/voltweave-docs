#include "MyGridPlayer.h"

#include "Components/VWVSwitchComponent.h"

void AMyGridPlayer::RequestToggle(UVWVSwitchComponent* Switch)
{
	if (IsValid(Switch))
	{
		ServerToggleSwitch(Switch);
	}
}

void AMyGridPlayer::ServerToggleSwitch_Implementation(UVWVSwitchComponent* Switch)
{
	// Never trust the client: check that the target exists and is within reach.
	if (!IsValid(Switch) || FVector::Dist(Switch->GetComponentLocation(), GetActorLocation()) > MaxReach)
	{
		return;
	}
	Switch->Toggle();
}
