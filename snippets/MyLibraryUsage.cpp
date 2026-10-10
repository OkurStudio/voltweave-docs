#include "MyLibraryUsage.h"

#include "VWVBlueprintLibrary.h"

void AMyLibraryUsage::BeginPlay()
{
	Super::BeginPlay();

	// Server: wire the first node of each Actor.
	if (HasAuthority())
	{
		UVWVBlueprintLibrary::ConnectActors(GeneratorActor, LampActor);
	}

	// Anywhere: does the lamp have power?
	const bool bLit = UVWVBlueprintLibrary::IsActorPowered(LampActor);

	// For a HUD: a readable text.
	const FText Text = UVWVBlueprintLibrary::FormatWatts(1500.f);
	UE_LOG(LogTemp, Log, TEXT("Lamp lit: %d, 1500 W is shown as %s"), bLit, *Text.ToString());
}
