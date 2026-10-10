#include "MyGridWatcher.h"

#include "VWVBlueprintLibrary.h"
#include "VWVGridSubsystem.h"

void AMyGridWatcher::BeginPlay()
{
	Super::BeginPlay();

	UVWVGridSubsystem* Grid = UVWVGridSubsystem::Get(this);
	if (!Grid || !Grid->IsSimulating())
	{
		// Network totals exist only where the grid is simulated: on the server or in a standalone game.
		return;
	}

	Grid->OnNetworkStateChanged.AddDynamic(this, &AMyGridWatcher::HandleNetworkStateChanged);
	LogAllNetworks();
}

void AMyGridWatcher::HandleNetworkStateChanged(const FVWVNetworkInfo& Network, EVWVNetworkState PreviousState)
{
	if (Network.State == EVWVNetworkState::Blackout)
	{
		UE_LOG(LogTemp, Warning, TEXT("Network %d is in a blackout"), Network.NetworkId);
	}
	else if (PreviousState == EVWVNetworkState::Blackout)
	{
		UE_LOG(LogTemp, Log, TEXT("Network %d recovered"), Network.NetworkId);
	}
}

void AMyGridWatcher::LogAllNetworks() const
{
	const UVWVGridSubsystem* Grid = UVWVGridSubsystem::Get(this);
	for (const FVWVNetworkInfo& Info : Grid->GetNetworks())
	{
		UE_LOG(LogTemp, Log, TEXT("Network %d: %d nodes, supply %s, demand %s"),
			Info.NetworkId, Info.NodeCount,
			*UVWVBlueprintLibrary::FormatWatts(Info.SupplyCapacityWatts).ToString(),
			*UVWVBlueprintLibrary::FormatWatts(Info.DemandWatts).ToString());
	}
}
