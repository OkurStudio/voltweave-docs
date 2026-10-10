#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "MyGridPlayer.generated.h"

class UVWVSwitchComponent;

/** A character that can ask the server to flip a switch. */
UCLASS()
class MYGAME_API AMyGridPlayer : public ACharacter
{
	GENERATED_BODY()

public:
	/** Call this on the owning client, for example from an input action. */
	void RequestToggle(UVWVSwitchComponent* Switch);

	UPROPERTY(EditAnywhere, Category = "Interaction")
	float MaxReach = 400.f;

protected:
	// Component functions are not RPCs: the client asks the server to act through an Actor it owns.
	UFUNCTION(Server, Reliable)
	void ServerToggleSwitch(UVWVSwitchComponent* Switch);
};
